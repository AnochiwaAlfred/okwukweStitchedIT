getList()

function decrease(id){
    cartValue = document.getElementById(id).value
    if (cartValue > 1){
        value = eval(cartValue) - 1
        document.getElementById(id).value = value
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
}