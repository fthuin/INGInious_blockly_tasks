/**
 * Blockly Games: Maze
 *
 * Copyright 2012 Google Inc.
 * https://github.com/google/blockly-games
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @fileoverview JavaScript for Blockly's Maze application.
 * @author fraser@google.com (Neil Fraser)
 */

var Problem = {};

var task_directory_path = "/course/" + course + "/" + taskid + "/";

Problem.MAP = [
    [0, 0, 0, 0],
    [0, 0, 0, 0]
];

Problem.SQUARE_TYPE = {
    SNOW: 0,
    PLAYER: 1
};

Problem.ROWS = Problem.MAP.length;
Problem.COLS = Problem.MAP[0].length;
Problem.SQUARE_SIZE = 50;
Problem.WIDTH = Problem.SQUARE_SIZE * Problem.COLS;
Problem.HEIGHT = Problem.SQUARE_SIZE * Problem.ROWS;

Problem.SKIN = {
    player: task_directory_path + 'images/americans.png',
    snow: task_directory_path + 'images/snow.png',
    swordSound: task_directory_path + 'sounds/sword.wav',
    sleepingSound: task_directory_path + 'sounds/sleeping.wav',
    winSound: task_directory_path + 'sounds/tadaa.wav'
};

Problem.svg = function(type) {
    return $(document.createElementNS(Blockly.SVG_NS, type));
};

Problem.drawMap = function() {
    var $svg = $("#blocklySvgZone");
    var x, y, tile;
    var scale = Math.max(Problem.ROWS, Problem.COLS) * Problem.SQUARE_SIZE;
    $svg[0].setAttribute('viewBox', '0 0 ' + scale + ' ' + scale);
    $svg.attr('style', '');

    var $square = Problem.svg('rect');
    $square.attr('width', Problem.WIDTH);
    $square.attr('height', Problem.HEIGHT);
    $square.attr('fill', '#555');
    $square.attr('stroke-width', 5);
    $square.attr('stroke', '#000');
    $svg.append($square);

    var $image;

    for (var i = 0; i < Problem.ROWS; i++) {
        for (var j = 0; j < Problem.COLS; j++) {
            var imagePath = "";
            switch(Problem.MAP[i][j]) {
                case Problem.SQUARE_TYPE.SNOW:
                    imagePath = Problem.SKIN.snow;
                    break;
                case Problem.SQUARE_TYPE.PLAYER:
                    imagePath = Problem.SKIN.player;
                    break;
            }

            $image = Problem.svg('image');
            $image[0].setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', Problem.SKIN.snow);
            $image.attr("height", Problem.SQUARE_SIZE);
            $image.attr("width", Problem.SQUARE_SIZE);
            $image.attr("x", j * Problem.SQUARE_SIZE);
            $image.attr("y", i * Problem.SQUARE_SIZE);
            $svg.append($image);
        }
    }
};

Problem.init = function() {
    if (typeof Blockly === "undefined" || typeof Blockly.getMainWorkspace() === "undefined" || Blockly.getMainWorkspace() === null) {
        console.warn("Maze.init() called but Blockly or workspace was not loaded.");
        window.setTimeout(Maze.init, 20);
        return;
    }

    Blockly.getMainWorkspace().loadAudio_(Problem.SKIN.swordSound, 'sword');
    Blockly.getMainWorkspace().loadAudio_(Problem.SKIN.sleepingSound, 'sleeping');
    Blockly.getMainWorkspace().loadAudio_(Problem.SKIN.winSound, 'win');

    Problem.drawMap();
};

if (document.getElementById('blocklySvgZone') !== null) {
    window.addEventListener('load', Problem.init);
} else {
    console.warn('Cannot find blocklySvgZone element.');
}
