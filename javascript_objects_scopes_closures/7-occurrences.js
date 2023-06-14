#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    var y = 0
    for (let i = 0; i < list.length; i++) {

        if (list[i] == searchElement) {

            y = y + 1

        }

    }
    console.log(y)

}


