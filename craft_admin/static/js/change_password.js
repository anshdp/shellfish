function change_password() {
    oldPassword = document.getElementById('exampleInputPassword').value
    newPassword = document.getElementById('exampleInputPassword1').value
    confirmPassword = document.getElementById('exampleInputPassword2').value
    console.log(confirmPassword, oldPassword, newPassword)
    if (newPassword != confirmPassword) {
        alert("Password Must be same")
    }
    $.ajax({
        url: '/craft_admin/changePassword',
        type: 'POST',
        data: {
            oldPassword,
            newPassword
        },
        success: function(response) {
            console.log(response)
            alert(response.message);
        }
    })
}