// ableton expects -2 thru 8
// api expects -1 thru 9

let letters = ["A", "B", "C", "D", "E", "F", "G"];
let newArr = [];
letter = letters[0];

rev = []

for (let letterIndex = 0; letterIndex < letters.length; letterIndex++) {
  for (let octave = 0; octave < 8; octave++) {
    if (letter == "B" || letter == "E") {
      newArr.push(letter + octave);
    } else {
      newArr.push(letter + octave);
      newArr.push(letter + "#" + octave);
    }
    letter = letters[letterIndex];
  }
}

function reverseString(str) {
    return str.split("").reverse().join("");
}


for (var i = 0; i < newArr.length; i++){
    rev.push(reverseString(newArr[i]));
}

console.log(rev)

// const apiFriendly = (str) => {
//     if (str.slice(2, 3) === '-' && str.slice(1,2) === "#"){
//         let newNum = Number(str.slice(-2)) + 1;
//         return str.slice(0,2)+newNum.toString()
//     }else if(str.slice(1,2) === "#"){
//         let newNum = Number(str.slice(2,3)) + 1;
//         return str.slice(0,2)+newNum.toString()
//     }
//     else{
//         let newNum = Number(str.slice(1)) + 1;
//         return str.slice(0, 1)+newNum.toString()
//     }
    
// } 

// console.log(apiFriendly("E-1"))
