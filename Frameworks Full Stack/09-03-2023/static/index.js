function Enviar() {
    
    var nome = document.getElementById("id-nome")
    var email = document.getElementById("id-email")
    var tel = document.getElementById("id-tel")

    if (nome.value != "") {
        alert(`Obrigado ${nome.value}, seus dados foram encaminhados com sucesso.\nNome: ${nome.value}\nEmail: ${email.value}\nTel: ${tel.value}`)
    }

}