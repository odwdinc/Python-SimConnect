L.Control.Rainviewer = L.Control.extend({
    options: {
        position: 'bottomleft',
        nextButtonText: '>',
        playStopButtonText: 'Play/Stop',
        prevButtonText: '<',
        positionSliderLabelText: "Hour:",
        opacitySliderLabelText: "Opacity:",
        animationInterval: 500,
        opacity: 0.5
    },

    onAdd: function (map) {
        /**
         * RainViewer radar animation part
         * @type {number[]}
         */
        this.timestamps = [];
        this.radarLayers = [];

        this.currentTimestamp;
        this.nextTimestamp;

        this.animationPosition = 0;
        this.animationTimer = false;

        this.rainviewerActive = false;

        this._map = map;

        this.container = L.DomUtil.create('div', 'leaflet-control-rainviewer leaflet-bar leaflet-control');

        this.link = L.DomUtil.create('a', 'leaflet-control-rainviewer-button leaflet-bar-part', this.container);
        this.link.href = '#';
        L.DomEvent.on(this.link, 'click', this.load, this);
        return this.container;

        /*return this.load(map);*/


    },

    load: function(map) {
        /**
         * Load actual radar animation frames this.timestamps from RainViewer API
         */
        var t = this;
        this.apiRequest = new XMLHttpRequest();
        this.apiRequest.open("GET", "https://tilecache.rainviewer.com/api/maps.json", true);
        this.apiRequest.onload = function (e) {

            // save available this.timestamps and show the latest frame: "-1" means "timestamp.lenght - 1"
            t.timestamps = JSON.parse(t.apiRequest.response);
            console.log(this);
            t.showFrame(-1);
        };
        this.apiRequest.send();

        /**
         * Animation functions
         * @param ts
         */

        L.DomUtil.addClass(this.container, 'leaflet-control-rainviewer-active');

        this.controlContainer = L.DomUtil.create('div', 'leaflet-control-rainviewer-container', this.container);

        this.prevButton = L.DomUtil.create('input', 'leaflet-control-rainviewer-prev leaflet-bar-part btn', this.controlContainer);
        this.prevButton.type = "button";
        this.prevButton.value = this.options.prevButtonText;
        L.DomEvent.on(this.prevButton, 'click', t.prev, this);
        L.DomEvent.disableClickPropagation(this.prevButton);

        this.startstopButton = L.DomUtil.create('input', 'leaflet-control-rainviewer-startstop leaflet-bar-part btn', this.controlContainer);
        this.startstopButton.type = "button";
        this.startstopButton.value = this.options.playStopButtonText;
        L.DomEvent.on(this.startstopButton, 'click', t.startstop, this);
        L.DomEvent.disableClickPropagation(this.startstopButton);

        this.nextButton = L.DomUtil.create('input', 'leaflet-control-rainviewer-next leaflet-bar-part btn', this.controlContainer);
        this.nextButton.type = "button";
        this.nextButton.value = this.options.nextButtonText;
        L.DomEvent.on(this.nextButton, 'click', t.next, this);
        L.DomEvent.disableClickPropagation(this.nextButton);

        this.positionSliderLabel = L.DomUtil.create('label', 'leaflet-control-rainviewer-label leaflet-bar-part', this.controlContainer);
        this.positionSliderLabel.for = "rainviewer-positionslider";
        this.positionSliderLabel.textContent = this.options.positionSliderLabelText;

        this.positionSlider = L.DomUtil.create('input', 'leaflet-control-rainviewer-positionslider leaflet-bar-part', this.controlContainer);
        this.positionSlider.type = "range";
        this.positionSlider.id = "rainviewer-positionslider";
        this.positionSlider.min = 0;
        this.positionSlider.max = 11;
        this.positionSlider.value = this.animationPosition;
        L.DomEvent.on(this.positionSlider, 'input', t.setPosition, this);
        L.DomEvent.disableClickPropagation(this.positionSlider);

        this.opacitySliderLabel = L.DomUtil.create('label', 'leaflet-control-rainviewer-label leaflet-bar-part', this.controlContainer);
        this.opacitySliderLabel.for = "rainviewer-opacityslider";
        this.opacitySliderLabel.textContent = this.options.opacitySliderLabelText;

        this.opacitySlider = L.DomUtil.create('input', 'leaflet-control-rainviewer-opacityslider leaflet-bar-part', this.controlContainer);
        this.opacitySlider.type = "range";
        this.opacitySlider.id = "rainviewer-opacityslider";
        this.opacitySlider.min = 0;
        this.opacitySlider.max = 100;
        this.opacitySlider.value = this.options.opacity*100;
        L.DomEvent.on(this.opacitySlider, 'input', t.setOpacity, this);
        L.DomEvent.disableClickPropagation(this.opacitySlider);


        this.closeButton = L.DomUtil.create('div', 'leaflet-control-rainviewer-close', this.container);
        L.DomEvent.on(this.closeButton, 'click', t.unload, this);

        var html = '<div id="timestamp" class="leaflet-control-rainviewer-timestamp"></div>'

        this.controlContainer.insertAdjacentHTML('beforeend', html);

        L.DomEvent.disableClickPropagation(this.controlContainer);

        /*return container;*/
    },

    unload: function(e) {
        L.DomUtil.remove(this.controlContainer);
        L.DomUtil.remove(this.closeButton);
        L.DomUtil.removeClass(this.container, 'leaflet-control-rainviewer-active');
        console.log(this.radarLayers);
        var radarLayers = this.radarLayers;
        var map = this._map;
        Object.keys(radarLayers).forEach(function (key) {
            if (map.hasLayer(radarLayers[key])) {
                map.removeLayer(radarLayers[key]);
            }
        });
    },

    addLayer: function(ts) {
        if (!this.radarLayers[ts]) {
            this.radarLayers[ts] = new L.TileLayer('https://tilecache.rainviewer.com/v2/radar/' + ts + '/256/{z}/{x}/{y}/2/1_1.png', {
                tileSize: 256,
                opacity: 0.001,
                transparent: true,
                attribution: '<a href="https://rainviewer.com" target="_blank">rainnviewer.com</a>',
                zIndex: ts
            });
        }
        if (!map.hasLayer(this.radarLayers[ts])) {
            map.addLayer(this.radarLayers[ts]);
        }
    },

    /**
     * Display particular frame of animation for the @position
     * If preloadOnly parameter is set to true, the frame layer only adds for the tiles preloading purpose
     * @param position
     * @param preloadOnly
     */
    changeRadarPosition: function(position, preloadOnly) {
        while (position >= this.timestamps.length) {
            position -= this.timestamps.length;
        }
        while (position < 0) {
            position += this.timestamps.length;
        }

        this.currentTimestamp = this.timestamps[this.animationPosition];
        this.nextTimestamp = this.timestamps[position];

        this.addLayer(this.nextTimestamp);

        if (preloadOnly) {
            return;
        }

        this.animationPosition = position;
        this.positionSlider.value = position;

        if (this.radarLayers[this.currentTimestamp]) {
            this.radarLayers[this.currentTimestamp].setOpacity(0);
        }
        this.radarLayers[this.nextTimestamp].setOpacity(this.options.opacity);

        document.getElementById("timestamp").innerHTML = (new Date(this.nextTimestamp * 1000)).toLocaleString();
    },

    /**
     * Check avialability and show particular frame position from the this.timestamps list
     */
    showFrame: function(nextPosition) {
        var preloadingDirection = nextPosition - this.animationPosition > 0 ? 1 : -1;

        this.changeRadarPosition(nextPosition);

        // preload next next frame (typically, +1 frame)
        // if don't do that, the animation will be blinking at the first loop
        this.changeRadarPosition(nextPosition + preloadingDirection, true);
    },

    /**
     * Stop the animation
     * Check if the animation timeout is set and clear it.
     */
    setOpacity: function(e){
        console.log(e.srcElement.value/100);
        if (this.radarLayers[this.currentTimestamp]) {
            this.radarLayers[this.currentTimestamp].setOpacity(e.srcElement.value/100);
        }
    },

    setPosition: function(e){
        this.showFrame(e.srcElement.value)
    },

    stop: function() {
        if (this.animationTimer) {
            clearTimeout(this.animationTimer);
            this.animationTimer = false;
            return true;
        }
        return false;
    },

    play: function() {
        this.showFrame(this.animationPosition + 1);

        // Main animation driver. Run this function every 500 ms
        this.animationTimer = setTimeout(function(){ this.play() }.bind(this), this.options.animationInterval);
    },

    playStop: function() {
        if (!this.stop()) {
            this.play();
        }
    },

    prev: function(e) {
        L.DomEvent.stopPropagation(e);
        L.DomEvent.preventDefault(e);
        this.stop();
        this.showFrame(this.animationPosition - 1);
        return
    },

    startstop: function(e) {
        L.DomEvent.stopPropagation(e);
        L.DomEvent.preventDefault(e);
        this.playStop()

    },

    next: function(e) {
        L.DomEvent.stopPropagation(e);
        L.DomEvent.preventDefault(e);
        this.stop();
        this.showFrame(this.animationPosition + 1);
        return
    },

    onRemove: function (map) {
        // Nothing to do here
    }
});

L.control.rainviewer = function (opts) {
    return new L.Control.Rainviewer(opts);
}