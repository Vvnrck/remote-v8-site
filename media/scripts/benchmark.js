// we get a list of parameters appended to the
// script before execution. I. e. a variable
// params is added:
// var params = '1,12,3.14,"wow"';

var number = parseInt(params);
for (var i = 0; i < 100; i++) {
    number *= 2.26;
    number /= 2.25;
}
toOutput(number);