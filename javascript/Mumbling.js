/* This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

////////////////////////////// solution //////////////////////////////////// */

function accum(s) {
  var strA = s.split("")
  var fin = strA[0].toUpperCase();
  for(i=1; i<strA.length; i++){
    fin += "-" + strA[i].toUpperCase() + strA[i].toLowerCase().repeat(i)
  }
  return fin
}





