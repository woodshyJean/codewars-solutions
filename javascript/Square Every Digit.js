/*Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

///////////////////////////////////////////// solution //////////////////////////////////////// */

function squareDigits(num){
  var number = num.toString().split('');
  var fin= ""
  for(i=0; i<number.length;i++){
    fin += (number[i]**2).toString();
  }
  return Number(fin);
}
