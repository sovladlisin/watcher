$(document).ready(function(){
      setInterval(function(){
            $.ajax({
                    url: "/myApp/admin/activations",
                    type: "GET",
                    success: function(response) {
                        $('#hehe').empty();
                        $('#hehe').append(response.template);
                        // if (response.calls != '0') {
                            if($("#notification-user").length != 0 && response.calls != '0') {
                                el = document.querySelector('#notification-user');
                                el.classList.add('show-count');
                                el.setAttribute('data-count', response.calls);
                            }
                             if($("#notification-admin-patients").length != 0 && response.new_activations != '0') {
                                el = document.querySelector('#notification-admin-patients');
                                el.classList.add('show-count');
                                el.setAttribute('data-count', response.new_activations);
                            }
                             if($("#notification-admin-users").length != 0 && response.new_users != '0') {
                                el = document.querySelector('#notification-admin-users');
                                el.classList.add('show-count');
                                el.setAttribute('data-count', response.new_users);
                            }
                    },
                    dataType: "json",
                    timeout: 2000
                });

    }, 3000);
});
