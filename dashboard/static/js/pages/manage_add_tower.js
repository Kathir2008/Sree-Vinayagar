$(document).ready(function() {

    console.log("Ready Go...")

    $("#upload-btn span").click(function() {
        $("#tower_image").click();
    });
    
    $(".Reset-Btn").click(function() {
        $("#tower_image").val("");
        $("#profile_image").attr("src", $("#profile_image").data("img"));
    });

    tower_image.onchange = evt => {
        const [file] = tower_image.files;
        if (file) {
            profile_image.src = URL.createObjectURL(file)
        }
    }

    $(".BackBtn").click(function() {
        $(".TowerCreation").hide();
        $(".TowerView").show();  
    });

    $("#createTowerBtn").click(function() {
        $(".TowerCreation").show();
        $(".TowerView").hide();
        $("#createTowerForm").trigger('reset')
        $("#towerId").val(0);
        $(".submitBtn").text("Register");
        $("#profile_image").attr("src", "../static/img/avatars/notower.jpg")
        $("#tower_image").attr('required', 'required');
    })

    
    towerTable();

    function towerTable() {
        (function rec(d) {
            $.each(d, function(k, v) {
                if (typeof v === 'object') return rec(v)
                if (isNaN(v) && typeof v === 'number') d[k] = '---';
            })
        })();

        if ($.fn.dataTable.isDataTable("#towerListDT")) {
            $("#towerListDT").DataTable().destroy();
        }

        var userListDatatable = $("#towerListDT").DataTable({
            responsive: true,
            paging: true,
            searching: false,
            "scrollY": false,
            "scrollCollapse": true,
            "pageLength": 10,
            "order": [0, "desc"],
            "bLengthChange": false,
            "scrollX": false,
            columnDefs: [
                {
                    "targets":0,
                    "visible":false,
                },
            ]

        })
    };


    $("#towerListDT").on("click", ".EditBtn", function() {

        $(".TowerCreation").show();
        $(".TowerView").hide();  

        var thisData = $(this).data("val") ;
        eval('var thistowerData = '+thisData);

        console.log(thistowerData)

        $("#towerId").val(thistowerData.id);
        $("#tower_id").val(thistowerData.tower_id)
        $("#functional_location").val(thistowerData.functional_location);
        $("#latitude").val(thistowerData.latitude);
        $("#longitude").val(thistowerData.longitude);
        $("#machine_capacity").val(thistowerData.machine_capacity);
        $("#tower_type").val(thistowerData.tower_type);
        $("#tower_model").val(thistowerData.tower_model);
        $("#blade_type").val(thistowerData.blade_type);
        $("#machine_height").val(thistowerData.machine_height);
        $("#panel").val(thistowerData.panel);
        $("#transformer").val(thistowerData.transformer);

        $("#tower_image").val("")

        $("#tower_image").removeAttr('required');

        $("#tower_image").attr("src" , "../media/"+thistowerData.tower_image)

        $(".submitBtn").text("Save Changes");
    })

})
