const numbers = [1, 45, 67, 75 , 5, 0, 40]
numbers.sort(function(a,b){
  return a -b
})

console.log(numbers)


numbers.sort((a,b) => a - b)
  .map((number)=> `Eu sou o numero ${number}`)
  .forEach((number) => {console.log(number)})

console.log("______________-________por letra _____________________________")

  var items = [
    { name: 'Edward', value: 21 },
    { name: 'Sharpe', value: 37 },
    { name: 'And', value: 45 },
    { name: 'The', value: -12 },
    { name: 'Magnetic' },
    { name: 'Zeros', value: 37 }
  ];
  items.sort(function (a, b) {
    if (a.name > b.name) {
      return 1;
    }
    if (a.name < b.name) {
      return -1;
    }
    // a must be equal to b
    return 0;
  });

  console.log(items)

 console.log("_______________________________por numero _____________________________________________")
  var itens = [
    { name: 'Edward', value: 21 },
    { name: 'Sharpe', value: 37 },
    { name: 'And', value: 45 },
    { name: 'The', value: -12 },
    { name: 'Magnetic' },
    { name: 'Zeros', value: 37 }
  ];
  itens.sort(function (a, b) {
    if (a.value > b.value) {
      return 1;
    }
    if (a.value < b.value) {
      return -1;
    }
    // a must be equal to b
    return 0;
  });

  console.log(itens)