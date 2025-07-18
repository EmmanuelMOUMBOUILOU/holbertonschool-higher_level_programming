document.querySelector('#add_item').addEventListener('click', function () {
  const newItem = document.createElement('li');  // Crée un nouveau <li>
  newItem.textContent = 'Item';                 // Ajoute le texte "Item"
  document.querySelector('.my_list').appendChild(newItem);  // L'ajoute à la liste
});
