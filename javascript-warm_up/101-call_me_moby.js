#!/usr/bin/node
exports.callMeMo = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
