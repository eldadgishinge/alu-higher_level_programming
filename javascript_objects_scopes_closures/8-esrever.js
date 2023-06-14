#!/usr/bin/node
exports.esrever = function (list) {
  const j = list.length - 1;
  const lest2 = [];
  for (let i = j; i >= 0; i--) {
    lest2.push(list[i]);
  }
  return lest2;
};
