$(document).ready(function() {

    // Mostrar y ocultar la imagen de la página principal
    $("#show_picture").hide();

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


  
});
