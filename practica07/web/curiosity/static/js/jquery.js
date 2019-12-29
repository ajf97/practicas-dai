$(document).ready(function() {

    // Desactivar botones por defecto

    $("#show_picture").hide();
    $("#light_mode").hide();
    
    // Mostrar y ocultar la imagen de la página principal

    $("#hide_picture").click(function(){

        $("#picture_header").hide();
        $("#hide_picture").hide();
        $("#show_picture").show();

    });

    $("#show_picture").click(function(){

        $("#picture_header").show();
        $("#hide_picture").show();
        $("#show_picture").hide();

    });

    // Modo claro y oscuro

    $("#dark_mode").click(function() {

        $("#light_mode").show();
        $("#dark_mode").hide();
        $("body").addClass("bg-dark");
        $("body").addClass("text-white");
        $(".list-group-item").addClass("list-group-item-dark");
        $(".card").addClass("bg-dark");

    });


    $("#light_mode").click(function() {

        $("#dark_mode").show();
        $("#light_mode").hide();
        $("body").removeClass("bg-dark");
        $("body").removeClass("text-white");
        $(".list-group-item").removeClass("list-group-item-dark");
        $(".card").removeClass("bg-dark");

    });

    // Aumentar y disminuir el tamaño de letra

    $("#increase_font").click(function() {

        var fontSize = parseInt($("body").css("font-size"));
        fontSize = fontSize + 1 + "px";
        $("body").css({'font-size':fontSize});

    });


    $("#decrease_font").click(function() {

        var fontSize = parseInt($("body").css("font-size"));
        fontSize = fontSize - 1 + "px";
        $("body").css({'font-size':fontSize});

    });


  
});
