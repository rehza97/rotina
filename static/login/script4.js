let signUpButton = document.getElementById('signUp');
let signInButton = document.getElementById('signIn');
let main = document.getElementById('main');

signUpButton.addEventListener('click', () => { 
    main.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => { 
    main.classList.remove('right-panel-active');
});