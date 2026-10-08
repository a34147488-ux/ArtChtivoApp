let stars = 0;

let level = 1;



const tg = window.Telegram.WebApp;

tg.expand();



let user = tg.initDataUnsafe.user;


if(user){

document.getElementById("username").innerHTML =
user.first_name;

}



function update(){


document.getElementById("stars").innerHTML =
stars+" ⭐";


document.getElementById("level").innerHTML =
level;


}




function mine(){


let power = level * 5;


stars += power;


let gain =
document.getElementById("gain");


gain.innerHTML =
"+"+power+" Stars";


gain.classList.remove("pop");


void gain.offsetWidth;


gain.classList.add("pop");


update();


}




update();
