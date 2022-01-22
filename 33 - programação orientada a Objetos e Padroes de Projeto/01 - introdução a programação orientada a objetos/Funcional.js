const numbers = [1, 45, 67, 75 , 5, 0, 40]

numbers.sort()
  .map((number)=> `Eu sou o numero ${number}`)
  .forEach((number) => {console.log(number)})
