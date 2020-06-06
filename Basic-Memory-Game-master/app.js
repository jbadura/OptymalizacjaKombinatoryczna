document.addEventListener('DOMContentLoaded', () => {
  // card options
  const cardArray = [
    {
      name: 'dziewczyna',
      img: 'images/dziewczyna.png'
    },
    {
      name: 'dziewczyna',
      img: 'images/dziewczyna.png'
    },
    {
      name: 'gwiazda',
      img: 'images/gwiazda.png'
    },
    {
      name: 'gwiazda',
      img: 'images/gwiazda.png'
    },
    {
      name: 'images',
      img: 'images/images.png'
    },
    {
      name: 'images',
      img: 'images/images.png'
    },
    {
      name: 'kostka',
      img: 'images/kostka.png'
    },
    {
      name: 'kostka',
      img: 'images/kostka.png'
    },
    {
      name: 'miecz',
      img: 'images/miecz.png'
    },
    {
      name: 'miecz',
      img: 'images/miecz.png'
    },
    {
      name: 'Minion',
      img: 'images/Minion.png'
    },
    {
      name: 'Minion',
      img: 'images/Minion.png'
    }
  ]

  // randomizing cards Array

  cardArray.sort(() => 0.5 - Math.random())

  const grid = document.querySelector('.grid') // showing Java where to look for a grid
  var cardsChosen = []
  var cardsChosenId = []
  var cardsWon = []
  const resultDisplay = document.querySelector('#result')

  // creating a board
  function createBoard () {
    for (let i = 0; i < cardArray.length; i++) { // for every card in Array
      var card = document.createElement('img') // we settle a value
      card.setAttribute('src', 'images/czarny.png') // and the attribute for the it's cover
      card.setAttribute('data-id', i) // as well as on it's face
      card.addEventListener('click', flipCard) //
      grid.appendChild(card) //
    }
  }

  // check for matches
  function checkForMatches () {
    var cards = document.querySelectorAll('img') // cards gets their value. All cards have their image
    const firstPick = cardsChosenId[0] // the card you will clisk first will be the first value in chosen Id array
    const secoundPick = cardsChosenId[1] // secound card will be nexr in that array
    if (cardsChosen[0] === cardsChosen[1]) { //
      alert('You found a match') //
      cards[firstPick].setAttribute('src', 'images/bialy.png') // both cards will get white cover
      cards[secoundPick].setAttribute('src', 'images/bialy.png')
      cardsWon.push(cardsChosen) // and program collects matched cards
    } else {
      cards[firstPick].setAttribute('src', 'images/czarny.png') // coming back to their original cover
      cards[secoundPick].setAttribute('src', 'images/czarny.png')
      alert('Sorry, try again')
    }
    cardsChosen = [] // clear the arrays to begin new matching
    cardsChosenId = []
    resultDisplay.textContent = cardsWon.length
    if (cardsWon.length === cardArray.length / 2) {
      resultDisplay.textContent = 'Congratulations! You found them all'
    }
  }

  // flip your card
  function flipCard () {
    var cardId = this.getAttribute('data-id') // poprzednia funkcja nadaje date-id ta ją przypisuje do danej karty
    cardsChosen.push(cardArray[cardId].name) // wypycha do pustego arrayu nazwe karty
    cardsChosenId.push(cardId) // jak również jej nowo powstałe ID
    this.setAttribute('src', cardArray[cardId].img) // to ustala nową wartość kart na src + obrazek z arrayu
    if (cardsChosen.length === 2) {
      setTimeout(checkForMatches, 500) // jak w nowym arrayu mamy wypushowane 2 karty -> odpala się timer półsekundowy i funckcja się kończy bo zawsze działa
    }
  }

  createBoard()
})
