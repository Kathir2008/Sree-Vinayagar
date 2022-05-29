$(document).ready(function() {

   

    $("#role").select2({
        placeholder : "Select Role",
        allowClear : false
    })

    $("#managed_by").select2({
        placeholder : "Managed By",
        allowClear : false
    })

    $("#region").select2({
        placeholder : "Select Region",
        allowClear : false
    })

    $("#status").select2({
        placeholder : "Select Status",
        allowClear : false
    })
    

  

    $(".BackBtn").click(function() {
        $(".UserCreation").hide();
        $(".UserView").show();  
    });

    $("#adduserBtn").click(function() {

        $(".UserCreation").show();
        $(".UserView").hide();  
                            
        $("#addUsersForm").trigger('reset')
        $(".password_label").text("Password")
        $("#userId").val(0);
        $(".statusRow").hide();
        $("#status").val('0');
        $(".submitBtn").text("Register");
        $("#profile_image").attr("src", "../static/img/avatars/noprofile.png");
        $("#password").attr('required', 'required');
        $("#confirm_password").attr('required', 'required');
        // $("#user_image").attr('required', 'required');

        $("#managed_by").val("").trigger("change")
        $("#role").val("").trigger("change")

        $("#managed_by_row").show();

        $('#length').removeClass('valid').addClass('invalid');
        $('#letter').removeClass('valid').addClass('invalid');
        $('#capital').removeClass('valid').addClass('invalid');
        $('#number').removeClass('valid').addClass('invalid');
        $('#specialchar').removeClass('valid').addClass('invalid');

    })

    
    userTable();

    function userTable() {
        (function rec(d) {
            $.each(d, function(k, v) {
                if (typeof v === 'object') return rec(v)
                if (isNaN(v) && typeof v === 'number') d[k] = '---';
            })
        })();

        if ($.fn.dataTable.isDataTable("#userListDT")) {
            $("#userListDT").DataTable().destroy();
        }

        var userListDatatable = $("#userListDT").DataTable({
            responsive: true,
            paging: true,
            searching: false,
            "scrollY": false,
            "scrollCollapse": true,
            "pageLength": 10,
            "bLengthChange": false,
            "scrollX": false,
            columnDefs: []

        })
    };


  
    var passwordFormat = /^((?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{:"<>?}\.\,\-\=\;\']).{8,})+$/

    $("#addUsersForm").submit(function(e) {
        var userPassword = $("#password").val();
        var confirmPassword = $("#confirm_password").val();

        if(userPassword.length > 0 && confirmPassword.length > 0)
        {
            if(passwordFormat.test(userPassword))
            {
                if(userPassword == confirmPassword)
                {
                    var userStatus = $("#status").val();

                    if (userStatus == 1) {
                        e.preventDefault()
                        Swal.fire({
                            icon: "warning",
                            html: '<div class="row" style="margin-top:15px">\
                                        <div class="col-md-12">\
                                                <div class= "titleSection text-center">\
                                                    <h4>Are You Sure to Inactive</h4>\
                                                </div>\
                                        </div >\
                                    </div >\
                                    <div class="row" style="margin-top:15px">\
                                        <div class="col-md-12">\
                                            <div class="confirmSection text-center">\
                                                <p style="line-height:1.5;font-size:20px"><span style="font-weight:bold">' + $("#firstname").val() + '</span> Cannot be Assigned anymore</p>\
                                            </div>\
                                        </div>\
                                    </div>',
                            showCloseButton: false,
                            showConfirmButton: true,
                            showCancelButton: true,
                            cancelButtonText: "Cancel",
                            cancelButtonColor: 'grey',
                            confirmButtonText: "Confirm",
                            confirmButtonColor: '#22CC62',
                            focusConfirm: false,

                        }).then(function(result) {
                            if (result.value == true) {
                                $("#addUsersForm").unbind('submit').submit()
                            } else if (result.dismiss == 'cancel') {
                                e.preventDefault()
                            }
                        })
                    } else {
                        return true
                    }
                }
                else
                {
                    iziToast.error({
                        timeout: 2500,
                        balloon: true,
                        overlay: true,
                        displayMode: 'once',
                        id: 'error',
                        title: 'Error',
                        zindex: 99999999,
                        message: '<b>Confirm Password is Invalid</b>',
                    });
                    return false
                }
            }
            else
            {
                $("#password").focus()

                return false
            }
            
        }

        else if(userPassword.length == 0 && confirmPassword.length > 0)
        {
            $("#password").focus()

            return false
        }

        else if(userPassword.length > 0 && confirmPassword.length == 0)
        {
            iziToast.error({
                timeout: 2500,
                balloon: true,
                overlay: true,
                displayMode: 'once',
                id: 'error',
                title: 'Error',
                zindex: 99999999,
                message: '<b>Confirm Password is Invalid</b>',
            });
            return false
        }

        else if(userPassword.length == 0 && confirmPassword.length == 0)
        {
            var userStatus = $("#status").val();

            if (userStatus == 1) {
                e.preventDefault();
                Swal.fire({
                    icon: "warning",
                    html: '<div class="row" style="margin-top:15px">\
                                <div class="col-md-12">\
                                        <div class= "titleSection text-center">\
                                            <h4>Are You Sure to Inactive</h4>\
                                        </div>\
                                </div >\
                            </div >\
                            <div class="row" style="margin-top:15px">\
                                <div class="col-md-12">\
                                    <div class="confirmSection text-center">\
                                        <p style="line-height:1.5;font-size:20px"><span style="font-weight:bold">' + $("#firstname").val() + '</span> Cannot be Assigned anymore</p>\
                                    </div>\
                                </div>\
                            </div>',
                    showCloseButton: false,
                    showConfirmButton: true,
                    showCancelButton: true,
                    cancelButtonText: "Cancel",
                    cancelButtonColor: 'grey',
                    confirmButtonText: "Confirm",
                    confirmButtonColor: '#22CC62',
                    focusConfirm: false,

                }).then(function(result) {
                    if (result.value == true) {
                        $("#addUsersForm").unbind('submit').submit()
                    } else if (result.dismiss == 'cancel') {
                        e.preventDefault()
                    }
                })
            } else {
                return true
            }
        }

})

    $("#userListDT").on("click", ".EditBtn", function() {
        $(".statusRow").show();

        $(".UserCreation").show();
        $(".UserView").hide();  

        var thisData = $(this).data("val");
        eval('var thisUserData = '+thisData);
        $("#userId").val(thisUserData.id);
        $("#firstname").val(thisUserData.name);
        $("#email").val(thisUserData.email);
        $("#phone").val(thisUserData.phone);
        $("#address").val(thisUserData.address);
        $("#district").val(thisUserData.district);

        var ddt = thisUserData.dob.split('-');
        $("#dob").val(ddt[0] +"-"+ ddt[1] +"-"+ ddt[2].slice(0,2));

        var mdt = thisUserData.marriagedate.split('-');
        $("#marriagedate").val(mdt[0] +"-"+ mdt[1] +"-"+ mdt[2].slice(0,2));
       
       
        $("#maritalstatus").val(thisUserData.maritalstatus);
        
        $("#status").val(thisUserData.status);

        $(".submitBtn").text("Save Changes");
    });

})
