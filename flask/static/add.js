document.addEventListener('DOMContentLoaded', () => {
    const addItemBtn = document.getElementById('add-item-btn');
    const itemInput = document.getElementById('item-input');
    const itemList = document.getElementById('item-list');
  
    let items = [];
  
    addItemBtn.addEventListener('click', () => {
      const newItem = itemInput.value.trim();
      if (newItem !== '') {
        items.push(newItem);
        renderList();
        itemInput.value = '';
        itemInput.focus();
      }
    });
  
    itemInput.addEventListener('keyup', (e) => {
      if (e.key === 'Enter') {
        addItemBtn.click();
      }
    });
  
    function renderList() {
      itemList.innerHTML = '';
      items.forEach((item) => {
        const li = document.createElement('li');
        li.textContent = item;
        itemList.appendChild(li);
      });
    }
  });
  