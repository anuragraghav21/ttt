$("#n_value").keyup(function(event) {
    if (event.keyCode === 13) {
        $("#retrieve").click();
    }
});

$('#retrieve').click(function(){
    var n = $('#n_value').val();
    $.ajax({
        url: '/retrieve/',
        type: 'GET',
        data: {
            n: n
        },
        success: function(response){
            data = response;
            if('Error' in response){
                $('#frequencies').hide();
                Materialize.toast('Invalid number', 2000);
                return;
            }
            var html_text = '<thead> \
                              <tr> \
                                  <th>Word</th> \
                                  <th>Count</th> \
                              </tr> \
                            </thead>';
            html_text += '<tbody>';
            for(row in response){
                html_text += '<tr><td>';
                html_text += response[row][1];
                html_text += '</td>'; 
                html_text += '<td>';
                html_text += response[row][0];
                html_text += '</td></tr>';
            }
            html_text += '</tbody>';
            $('#frequencies').html(html_text);
            $('#frequencies').show();
        },
        error: function(){
            $('#frequencies').hide();
            Materialize.toast('Something went wrong!', 2000);
        }
    });
});