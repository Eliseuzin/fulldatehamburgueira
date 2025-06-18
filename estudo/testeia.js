const Menugeral = document.getElementById("menu");
// console.log(Menugeral);
const Meucarrinho = document.getElementById("meucarrinho");
const dentrodocarrinho = document.getElementById("dentrodocarrinho");
const submeucarrinho = document.getElementById("submeucarrinho");
const subdentrodocarrinho = document.getElementById("subdentrodocarrinho");
const Valortotal = document.getElementById("valortotal");
const pagarmercadopago=document.getElementById("pagar")
const Fechar = document.getElementById("Fechar");
const Finalizar = document.getElementById("Finalizar");
const Quantidadecarinho = document.getElementById("quantidadecarinho");
const Addressinput = document.getElementById("address");
const addressnome=document.getElementById("addressnome")
const addressphone=document.getElementById("addressphone");
const Addresswarninput = document.getElementById("address-warn");
const Addresswarninputnome = document.getElementById("address-warnnome");
const Addresswarninputphone = document.getElementById("address-warnphone");
const itensaddnocarrinho = document.getElementById("itensadd");
const subbottom = document.getElementById("subbottom");

const out = document.getElementById("out");
const Finish = document.getElementById("Finish");

var listcar=[];
subbottom.style.display="none";

//abrir o carrinho
Meucarrinho.addEventListener("click",function(){
  dentrodocarrinho.style.display="block";
})

//fechar o carrinho, com click fora
dentrodocarrinho.addEventListener("click",function(event){
if (event.target===dentrodocarrinho){
  dentrodocarrinho.style.display="none";
}
})
subbottom.addEventListener("click", function(event){
  if(event.target===out){
    dentrodocarrinho.style.display="none";
  }
})
//fechar o carrinho com click de fechar
dentrodocarrinho.addEventListener("click",function(event){
  if(event.target===Fechar){
    dentrodocarrinho.style.display="none";
  }
})

Menugeral.addEventListener("click", function (event) {
  // console.log(event.target);

  var parentButtom = event.target.closest(".addcart");

  // console.log(parentButtom);

  if (parentButtom) {
    const name = parentButtom.getAttribute("data-name");
    const price = parseFloat(parentButtom.getAttribute("data-price"));

    // console.log(name);
    // console.log(price);

    //adicionar no carrinho

    addinmycar(name, price);
    // remoitenscarrinho(name);
  }
});
// função para adicionar no carrinho
function addinmycar(name, price) {
  // alert(` item is ${name} and  price is ${price}`);

  const checklistcar = listcar.find((item) => item.name === name);

  if (checklistcar) {
    //se o item já existe aumenta a quantidade +1
    // console.log(checklistcar);
    checklistcar.quantity += 1;

    // return;
  } else {
    listcar.push({
      name,
      price,
      quantity: 1,
    });
  }
  updatecarrinho();
  subbottom.style.display = "block";
}

//atualizar o carrinho
let total = 0;

function updatecarrinho() {
  submeucarrinho.innerHTML = "";
  // let total = 0;

  listcar.forEach((item) => {
    const incluirosprodutos = document.createElement("div");
    incluirosprodutos.setAttribute("class", "estilizarprodutos");

    incluirosprodutos.innerHTML = `<div>
        <div>
            <p>${item.name}</p>
            <p> Qtds:${item.quantity}</p>
            <p>R$:${item.price.toFixed(2)}</p>

        </div>

           <buttom  class='removeritem' data-name="${
             item.name
           }">Remover</buttom>
      
    </div>`;
    total += item.price * item.quantity;
    submeucarrinho.appendChild(incluirosprodutos);
  });

  //valor total do carrinho
  // Valortotal.textContent = `Total a Pagar: ${total.toLocaleString("pt-BR", {
  //   style: "currency",
  //   currency: "BRL",
  // })}`;
    //valor total do carrinho
    pagarmercadopago.textContent = `Pagar com Mercado Pago: ${total.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
    })}`;
  // valorpedido()

  Quantidadecarinho.innerHTML = listcar.length;
}
// total += item.price * item.quantity;
// submeucarrinho.appendChild(incluirosprodutos);

//funcao valor total do carrino
// function valorpedido(){
//   pagarmercadopago.textContent = `Pagar com Mercado Pago: ${total.toLocaleString("pt-BR", {
//     style: "currency",
//     currency: "BRL",
//     })}`;
// }

// funçao para remover item
submeucarrinho.addEventListener("click", function (event) {
  if (event.target.classList.contains("removeritem")) {
    const name = event.target.getAttribute("data-name");
    console.log(name);
    //chamar funçao
    removeritens(name);
  }
});

function removeritens(name) {
  const index = listcar.findIndex((item) => item.name === name);

  if (index !== -1) {
    const item = listcar[index];
    // console.log(item);

    if (item.quantity > 1) {
      item.quantity -= 1;
      updatecarrinho();
      return;
    } else {
      listcar.splice(index, 1);
      updatecarrinho();
    }
  }
}

Addressinput.addEventListener("input", function (event) {
  var inputValue = event.target.value;
  // if (inputValue !== "") {
  //   Addresswarninput.style.visibility = "hidden";
  // }
});
Finish.addEventListener("click", function () {
  // const isOpen = verificaropen();
  // if (!isOpen) {
  //   //importaçao mensagem loja fechada
  //   Toastify({
  //     text: "Desculpe, a pizzaria está fechada!",
  //     duration: 4000,
  //     close: true,
  //     gravity: "top", // `top` or `bottom`
  //     position: "left", // `left`, `center` or `right`
  //     stopOnFocus: true, // Prevents dismissing of toast on hover
  //     style: {
  //       background: "linear-gradient(to right,rgba(255, 0, 0, 0.13),rgb(255, 0, 0))",
  //     },
  //   }).showToast();
  //   return;
  // }

  if (listcar.length === 0) return;

  if (Addressinput.value === "") {
    Addresswarninput.style.display = "block";
    Addresswarninput.innerText = "O endereço está vazio!";
    return;
  } else if (Addressinput.value.length <= 3) {
    Addresswarninput.style.display = "block";
    Addresswarninput.innerText =
      "O endereço precisa ter no minimo 3 caracteres";
    return;
  } else {
    Addresswarninput.style.display = "none";
  }

  if(addressnome.value===""){
    Addresswarninputnome.style.display="block"
    Addresswarninputnome.innerText="Um nome valido, por favor!!!"
    return;
  }else if(addressnome.value.length<=3){
    Addresswarninputnome.style.display="block"
    Addresswarninputnome.innerText="Nome precisa ter mais de 3 caracteres! "
    return;
  }else{
    Addresswarninputnome.style.display="none"
  }
  if(addressphone.value===""){
    Addresswarninputphone.style.display="block"
    Addresswarninputphone.innerText="Um numero valido, por favor!!!"
    return;
  } 
  else if (addressphone.value.length<=10){
    Addresswarninputphone.style.display="block"
    Addresswarninputphone.innerText="Precisa ter 11 numeros "
    Addresswarninputphone.innerText="Ex.:31999990000 "
    return;
  }else if (addressphone.value.length>11){
    Addresswarninputphone.style.display="block"
    Addresswarninputphone.innerText="Precisa ter 11 numeros "
    return;
  }else{
    Addresswarninputphone.style.display="none"
  }

  //ENVIAR PARA O WHATSAPP
  // console.log(listcar);

  // const listcaritens = listcar
  //   .map((item) => {
  //     return `${item.name}, Quantidade:(${item.quantity}), Preço R$:(${item.price})|***|`;
  //   })
  //   .join("");

  // const messagem = encodeURIComponent(listcaritens);
  // const celular = "31994174975";

  // window.open(
  //   `https://wa.me/${celular}?text=${messagem}, ${Valortotal.textContent},// Nome: ${addressnome.value},// Endereço: ${Addressinput.value},// Celular: ${addressphone.value}`,
  //   "_blank"
  // );
  // listcar.length = [];
  // updatecarrinho();
  // // console.log(listcaritens);

});

// let total = 29.90; // ou algum valor dinâmico vindo do carrinho

document.getElementById("pagar").addEventListener("click", function () {

  pagarmercadopago.textContent = `Pagar com Mercado Pago: ${total.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  })}`;

  // Extrai o número do texto
  const texto = pagarmercadopago.textContent;
  const valorString = texto.match(/[\d,.]+/)[0]; // extrai "29,90"
  const valorNumerico = parseFloat(valorString.replace(".", "").replace(",", ".")); // converte para 29.90

  fetch("https://b1e0-2804-540-153-2d00-d4da-ebe0-759a-2fb6.ngrok-free.app/criar_pagamento", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      titulo: "Pedido Teste",
      preco: valorNumerico
    })
  })
    .then(response => response.json())
    .then(data => {
      if (data.init_point) {
        window.location.href = data.init_point;
      } else {
        alert("Erro ao gerar link de pagamento.");
      }
    })
    .catch(error => {
      console.error("Erro na requisição:", error);
    });
});

  // pagarmercadopago.textContent = `Pagar com Mercado Pago: ${total.toLocaleString("pt-BR", {
  //   style: "currency",
  //   currency: "BRL",
  //   })}`;

// document.getElementById("pagar").addEventListener("click", function () {

//     pagarmercadopago.textContent = `Pagar com Mercado Pago: ${total.toLocaleString("pt-BR", {
//     style: "currency",
//     currency: "BRL",
//     })}`;

//   fetch("https://b1e0-2804-540-153-2d00-d4da-ebe0-759a-2fb6.ngrok-free.app/criar_pagamento", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json"
//     },
//     body: JSON.stringify({
//       titulo: "Pedido Teste",
//       preco: pagarmercadopago
//     })
//   })
//     .then(response => response.json())
//     .then(data => {
//       if (data.init_point) {
//         window.location.href = data.init_point;
//       } else {
//         alert("Erro ao gerar link de pagamento.");
//       }
//     })
//     .catch(error => {
//       console.error("Erro na requisição:", error);
//     });
// });
