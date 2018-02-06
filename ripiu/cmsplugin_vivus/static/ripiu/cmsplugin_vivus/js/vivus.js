"use strict";

(function () {
    var VivusAnimation = (function () {
        /**
         * Helper function that retrieves a data-attribute value.
         *
         * @function getAttr
         * @param {HTMLElement} element single document node
         * @param {String} data data-attribute to retrieve
         * @return {String} value returns the value from the data-attribute
         */
        function getAttr(element, data) {
            var value = element.getAttribute("data-" + data);

            // true/false values need to be parsed from string to boolean
            // from the attributes data
            if (value === "true") {
                return true;
            } else if (value === "false") {
                return false;
            } else if (value === "null") {
                return null;
            }
            return value;
        }

        /**
         * Configures and starts Vivus.
         *
         * @class VivusAnimation
         * @constructor
         * @param {HTMLElement} container single document node
         */
        function VivusAnimationConstructor(container) {
            this.container = container;
            this.settings = {
                type: getAttr(container, "animation-type"),
                start: getAttr(container, "start"),
                duration: parseInt(getAttr(container, "duration")),
                delay: parseInt(getAttr(container, "delay")),
                dashGap: parseInt(getAttr(container, "dash-gap")),
                forceRender: getAttr(container, "force-render"),
                reverseStack: getAttr(container, "reverse-stack"),
                selfDestroy: getAttr(container, "self-destroy")
            };
            console.log(this.settings);
            new Vivus(this.container, this.settings);
        }
        return VivusAnimationConstructor;
    })();

    window.addEventListener("load", function () {
        var elements = document.getElementsByClassName("ripiu-vivus");
        elements = [].slice.call(elements);
        elements.forEach(function (element) {
            new VivusAnimation(element);
            // new Vivus(element, {duration: 200});
        })
    })
})();
