$(document).ready(function() {

    var districtData = ["Ariyalur","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode",
                "Kanchipuram","Kanyakumari","Karur","Krishnagiri","Madurai","Nagapattinam","Namakkal",
                "Nilgiris","Perambalur","Pudukkottai","Ramanathapuram","Salem","Sivaganga","Thanjavur",
                "Theni","Thoothukudi","Tiruchirappalli","Tirunelveli","Tiruppur","Tiruvallur","Tiruvannamalai",
                "Tiruvarur","Vellore","Viluppuram","Virudhunagar"];

        
    for(var i = 0; i < districtData.length; i++){
        var htmlString = htmlString+"<option value='"+ districtData[i] +"'>"+ districtData[i] +"</option>";
    }
    $(".district_list_select2").html(htmlString);


    // Go Back Button 

    $(".BackBtn").click(function() {
        $(".RegionCreation").hide();
        $(".RegionView").show();  
        $(".ExpenseCreation").hide();
        $(".ExpenseView").show();  
    });

    // Pooja Fn
    $("#addregionBtn").click(function() {

        $(".RegionCreation").show();
        $(".RegionView").hide();  
                            
        $("#addRegionForm").trigger('reset')
        $("#regionId").val("0")

        // $("#district").val("Ariyalur").trigger("change")
    })

    // Expense Fn
    $("#addExpenseBtn").click(function() {

        $(".ExpenseCreation").show();
        $(".ExpenseView").hide();  
                            
        $("#addExpenseBtn").trigger('reset')
        $("#expenseId").val("0")

        $("#district").val("Ariyalur").trigger("change")
    })
    // Income fn
    
    $("#addIncomeBtn").click(function() {

        $(".IncomeCreation").show();
        $(".IncomeView").hide();  
                            
        $("#addIncomeBtn").trigger('reset')
        $("#incomeId").val("0")

        $("#district").val("Ariyalur").trigger("change")
    })

    $(".district_list_select2").select2({
        placeholder : "Select District",
        allowClear : true
    })

    



    regionTable();

    function regionTable() {
        (function rec(d) {
            $.each(d, function(k, v) {
                if (typeof v === 'object') return rec(v)
                if (isNaN(v) && typeof v === 'number') d[k] = '---';
            })
        })();

        if ($.fn.dataTable.isDataTable("#regionListDT")) {
            $("#regionListDT").DataTable().destroy();
        }

        var regionListDatatable = $("#regionListDT").DataTable({
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


    $("#regionListDT").on("click", ".EditBtn", function() {

        $(".RegionCreation").show();
        $(".RegionView").hide();  

        var thisData = $(this).data("val");

        eval('var thisregionData = '+thisData);

        $("#regionId").val(thisregionData.id);
        $("#name").val(thisregionData.name);
        $("#amount").val(thisregionData.amount);
        $("#desc").val(thisregionData.desc);

        $(".submitBtn").text("Save Changes");
    })
    $("#ExpenseListDT").on("click", ".EditBtn", function() {

        $(".ExpenseCreation").show();
        $(".ExpenseView").hide();  

        var thisData = $(this).data("val");

        eval('var thisexpenseData = '+thisData);

        // $("#regionId").val(thisexpenseData.id);
        $("#date").val(thisexpenseData.date);
        $("#desc").val(thisexpenseData.description);
        $("#amount").val(thisexpenseData.amount);
        $("#notes").val(thisexpenseData.notes);

        $(".submitBtn").text("Save Changes");
    })

 

})
