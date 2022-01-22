const numbers = [1, 45, 67, 75 , 5, 0, 40]
numbers.sort(function(a,b){
  return a -b
})

console.log(numbers)


numbers.sort((a,b) => a - b)
  .map((number)=> `Eu sou o numero ${number}`)
  .forEach((number) => {console.log(number)})
