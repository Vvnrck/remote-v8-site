// we get a list of parameters appended to the
// script before execution. I. e. a variable
// params is added:
// var params = '1,12,3.14,"wow"';

var number = Number(params);
for (var i = 0; i < 10000; i++) {
    number *= 2.255;
    number /= 2.25;
}
toOutput(number);