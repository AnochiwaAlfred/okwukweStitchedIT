getList()

function decrease(id){
    cartValue = document.getElementById(id).value
    if (cartValue > 1){
        value = eval(cartValue) - 1
        document.getElementById(id).value = value

        user_id = document.getElementById(id).dataset.user
        product_id = document.getElementById(id).dataset.product
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        fetch(`../../../cart/${user_id}/${product_id}/update-cart`, {
            method:'POST',
            headers:{'Content-Type':'application/json',
            'X-CSRFToken': csrfToken
        },
        body:value
        })
        .then(response => {
            if (response.ok) {
            console.log('Value submitted!');
            } else {
            console.error('Failed to submit value');
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });

}else{
        document.getElementById(id).value = 1
    }
    getList()
}




function increase(id){
    cartValue = document.getElementById(id).value
    itemQuantity = document.getElementById(id).dataset.quantity
    if (cartValue < itemQuantity){
        value = eval(cartValue) + 1
        document.getElementById(id).value = value
        
        user_id = document.getElementById(id).dataset.user
        product_id = document.getElementById(id).dataset.product
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        fetch(`../../../cart/${user_id}/${product_id}/update-cart`, {
            method:'POST',
            headers:{'Content-Type':'application/json',
            'X-CSRFToken': csrfToken
        },
        body:value
        })
        .then(response => {
            if (response.ok) {
            console.log('Value submitted!');
            } else {
            console.error('Failed to submit value');
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });

}else{
        document.getElementById(id).value = itemQuantity
    }
    getList()
}



function getList(){
    product = 0
    priceQueryList = document.querySelectorAll('.actual-price')
    priceList = []
    for (const i of priceQueryList) {
        priceList.push(eval(i.innerHTML))
    }
    quantityQueryList = document.querySelectorAll('.item-quantity')
    quantityList = []
    for (const i of quantityQueryList) {
        quantityList.push(eval(i.value))
    }

    if (priceList.length == quantityList.length){
        productList = []
        for (let i = 0; i < priceList.length; i++) {
            productList.push(priceList[i]*quantityList[i])
          }
        for (let i = 0; i < productList.length; i++) {
            product += productList[i]
        }
    }
    total = document.querySelector('#total')
    total.innerHTML = product
    updateOrder()
}



function updateOrder(){
    total = document.getElementById('total').innerHTML
    document.getElementById('order-btn').innerHTML=total
    mainUpdate()
}


function mainUpdate(){    
    const quantityInputsList =  document.getElementsByClassName('item-quantity');
    for (let i = 0; i < quantityInputsList.length; i++) {
        const quantityInput = quantityInputsList[i];
        
        quantityInput.addEventListener('input', function(event){
            const value=event.target.value
            const cleanValue = value.replace(/\D/g, '')
            event.target.value=cleanValue
        })
        
        quantityInput.addEventListener('input', getList);

        quantityInput.addEventListener('input', function(){
            const inputValue = this.value
            user_id = quantityInput.dataset.user
            product_id = quantityInput.dataset.product
            const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
            fetch(`../../../cart/${user_id}/${product_id}/update-cart`, {
                method:'POST',
                headers:{'Content-Type':'application/json',
                'X-CSRFToken': csrfToken
            },
            body:inputValue
            })
            .then(response => {
                if (response.ok) {
                console.log('Value submitted!');
                } else {
                console.error('Failed to submit value');
                }
            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
        })
    }
}

