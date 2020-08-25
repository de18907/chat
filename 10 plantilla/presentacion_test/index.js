var valor = 0;
var respuesta = 0;
//cuando precione y el parametro es igual a 1 o a -
function cambiar(parametro, numero){
//sumatorio
//todo este es mi codigo lo pudiera hacer mejos pero no me dio el tiempo
respuesta = Number(respuesta) + Number(numero);
    //llamo al elemento section
    secciones = document.getElementsByTagName('section');
    //si precionas a siguiente sera verdadero(=1) y si preciona hacia atras
    if(parametro > 0){
        //el secciones que sigue
        if(secciones[valor+1]){
        valor++;
        //quitar atributo
        diapositiva(secciones);
        //cambiar atributo a visible deacuerdo a la posición
        secciones[valor].setAttribute('class', 'visible');
        }else{
//resultado final
if(respuesta == 100 || respuesta == 110 || respuesta == 120 || respuesta == 130 || respuesta == 140 || respuesta == 150 || respuesta == 160){
    alert('Tu total es de ' + respuesta + ' de 100 a 160. Estarás viviendo en modo ahorrativo.\n' + 'quizas no seas rico en cuanto al dinero pero encuanto tener aventuras, tener recuerdos, estar rodeado de amigos seras mas rico que bill gates en dinero. El dinero no es tu prioridad numero uno y no eres muy cuidadoso al respeto, sueles gastar mas de lo que puedes pagar sin pensar en la consecuencia solo porque te da alegria.');
}else if(respuesta == 170 || respuesta == 180 || respuesta == 190 || respuesta == 200 || respuesta == 210 || respuesta == 220 || respuesta == 230){
    alert('Tu total es de ' + respuesta + ' de 180 a 240 .Viviaras Bastante cómodo.\n'+'siempre tendras lo suficiente para pagar las facturas, comer fuera de vez en cuando y comprar cosas de buena calidad. Sabes que el dinero llega a los que trabajan duro por lo que siempre planificas tus gastos y no tomas decisiones inracionales. Suana bien, verdad?');
}else if(respuesta == 240 || respuesta == 250 || respuesta == 260 || respuesta == 270 || respuesta == 280 || respuesta == 290 || respuesta == 300){
    alert('Tu total es de ' + respuesta + ' 240 a 300 . Felicidades, seras un futuro Rockefeller!\n'+'podras nadar en tu propia piscina de oro, el dinero lo es todo para ti y estas listo para darlo todo por tenerlo todo, cuentas cada centavo para multiplicar lo que ya tienes eres muy trabajador y decidido con ese espiritu emprendedor para hacer algo de la nada');
}
        }
    //sera falso(=0)
    }else{
        if(secciones[valor-1]){
            valor = 0;
            respuesta = 0;
            diapositiva(secciones);
            //nuevo atributo
            secciones[valor].setAttribute('class', 'visible');
        }else{
            alert('Ya estas en inicio');
        }
    }
}
function diapositiva(secciones){
    for(z=0; z < secciones.length; z++){
       secciones[z].removeAttribute('class');
    }
}