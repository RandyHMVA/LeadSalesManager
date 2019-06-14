$(()=> {
  /*
    * Setting datepicker inputs on the start of the search page
    */
    var dateFormat = "yy-mm-dd",
      from = $( "#from" )
        .datepicker({
          defaultDate: "+1w",
          changeMonth: true,
          numberOfMonths: 3,
          dateFormat: "yy-mm-dd",
          showAnim: "slide"
        })
        .on( "change", function() {
          to.datepicker( "option", "minDate", getDate( this ) );
        }),
      to = $( "#to" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3,
        dateFormat: "yy-mm-dd",
        showAnim: "slide"
      })
      .on( "change", function() {
        from.datepicker( "option", "maxDate", getDate( this ) );
      });
 
    function getDate( element ) {
      var date;
      try {
        date = $.datepicker.parseDate( dateFormat, element.value );
      } catch( error ) {
        date = null;
      }
 
      return date;
    }
////FOR LEAD SEARCH
  /*
    * Really long chain here I need to work on a bit to make better
    * Calls search on field and/or date range and outputs a table
    */
  $('#searcho').click(function() {
    var thelist = $('.ssearchList').val();
        if(thelist === 'ech'){
           if($('.fromdate').val()== '' && $('.todate').val()== ''){
           }else if($('.fromdate').val()== ''){
            var fromValue = '1997-06-05 00:00:00';
            var toValue = $('.todate').val() + ' 23:59:59';
            $.getJSON($SCRIPT_ROOT + '/daterange', {
                fromDate: fromValue,
                toDate: toValue
              }, function(data) {
                  var table = $.makeTable(data);
                  $("#searchcontainer").html(table);
              });
           }else if($('.todate').val()== ''){
            var fromValue = $('.fromdate').val() + ' 00:00:00';
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0'); 
            var yyyy = today.getFullYear();
            today = yyyy + '-' + mm + '-' + dd;
            var toValue = today + ' 23:59:59';
            $.getJSON($SCRIPT_ROOT + '/daterange', {
                fromDate: fromValue,
                toDate: toValue
              }, function(data) {
                  var table = $.makeTable(data);
                  $("#searchcontainer").html(table);
              });
           }else{
              var fromValue = $('.fromdate').val() + ' 00:00:00';
              var toValue = $('.todate').val() + ' 23:59:59';
              $.getJSON($SCRIPT_ROOT + '/daterange', {
                  fromDate: fromValue,
                  toDate: toValue
                }, function(data) {
                    var table = $.makeTable(data);
                    $("#searchcontainer").html(table);
                });
           }
        }else if($('.fromdate').val()== '' && $('.todate').val()== ''){
          $('#searchcontainer').empty();
            var thesearch = $('#searchin').val();
          $.getJSON($SCRIPT_ROOT + '/' + thelist, {
            search: thesearch
          }, function(data) {
              var table = $.makeTable(data);
              $("#searchcontainer").html(table);
          });
        }else if($('.todate').val()== ''){
          var fromValue = $('.fromdate').val() + ' 00:00:00';
          var today = new Date();
          var dd = String(today.getDate()).padStart(2, '0');
          var mm = String(today.getMonth() + 1).padStart(2, '0'); 
          var yyyy = today.getFullYear();
          today = yyyy + '-' + mm + '-' + dd;
          var toValue = today + ' 23:59:59';
          $('#searchcontainer').empty();
            var thesearch = $('#searchin').val();
          $.getJSON($SCRIPT_ROOT + '/date' + thelist, {
            search: thesearch,
            fromDate: fromValue,
            toDate: toValue
          }, function(data) {
              var table = $.makeTable(data);
              $("#searchcontainer").html(table);
          });
        }else if($('.fromdate').val()== ''){
          var fromValue = '1997-06-05 00:00:00';
          var toValue = $('.todate').val() + ' 23:59:59';
          $('#searchcontainer').empty();
          var thesearch = $('#searchin').val();
          $.getJSON($SCRIPT_ROOT + '/date' + thelist, {
            search: thesearch,
            fromDate: fromValue,
            toDate: toValue
          }, function(data) {
              var table = $.makeTable(data);
              $("#searchcontainer").html(table);
          });
      }else{
        var fromValue = $('.fromdate').val() + ' 00:00:00';
        var toValue = $('.todate').val() + ' 23:59:59';
        $('#searchcontainer').empty();
        var thesearch = $('#searchin').val();
        $.getJSON($SCRIPT_ROOT + '/date' + thelist, {
          search: thesearch,
          fromDate: fromValue,
          toDate: toValue
        }, function(data) {
            var table = $.makeTable(data);
            $("#searchcontainer").html(table);
        });
      }
  });
///FOR SALE SEARCH
  $('#saleo').click(function() {
    var thelist = $('.ssaleList').val();
        if(thelist === 'ech'){
           if($('.fromdate').val()== '' && $('.todate').val()== ''){
           }else if($('.fromdate').val()== ''){
            var fromValue = '1997-06-05';
            var toValue = $('.todate').val();
            $.getJSON($SCRIPT_ROOT + '/saledaterange', {
                fromDate: fromValue,
                toDate: toValue
              }, function(data) {
                  var table = $.makeTable(data,true);
                  $("#salecontainer").html(table);
              });
           }else if($('.todate').val()== ''){
            var fromValue = $('.fromdate').val();
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0'); 
            var yyyy = today.getFullYear();
            today = yyyy + '-' + mm + '-' + dd;
            var toValue = today + ' 23:59:59';
            $.getJSON($SCRIPT_ROOT + '/saledaterange', {
                fromDate: fromValue,
                toDate: toValue
              }, function(data) {
                  var table = $.makeTable(data,true);
                  $("#salecontainer").html(table);
              });
           }else{
              var fromValue = $('.fromdate').val();
              var toValue = $('.todate').val();
              $.getJSON($SCRIPT_ROOT + '/saledaterange', {
                  fromDate: fromValue,
                  toDate: toValue
                }, function(data) {
                    var table = $.makeTable(data,true);
                    $("#salecontainer").html(table);
                });
           }
        }else if($('.fromdate').val()== '' && $('.todate').val()== ''){
          $('#salecontainer').empty();
            var thesearch = $('#searchsalein').val();
          $.getJSON($SCRIPT_ROOT + '/sale' + thelist, {
            search: thesearch
          }, function(data) {
              var table = $.makeTable(data,true);
              $("#salecontainer").html(table);
          });
        }else if($('.todate').val()== ''){
          var fromValue = $('.fromdate').val();
          var today = new Date();
          var dd = String(today.getDate()).padStart(2, '0');
          var mm = String(today.getMonth() + 1).padStart(2, '0'); 
          var yyyy = today.getFullYear();
          today = yyyy + '-' + mm + '-' + dd;
          var toValue = today;
          $('#salecontainer').empty();
            var thesearch = $('#searchsalein').val();
          $.getJSON($SCRIPT_ROOT + '/datesale' + thelist, {
            search: thesearch,
            fromDate: fromValue,
            toDate: toValue
          }, function(data) {
              var table = $.makeTable(data,true);
              $("#salecontainer").html(table);
          });
        }else if($('.fromdate').val()== ''){
          var fromValue = '1997-06-05';
          var toValue = $('.todate').val();
          $('#salecontainer').empty();
          var thesearch = $('#searchsalein').val();
          $.getJSON($SCRIPT_ROOT + '/datesale' + thelist, {
            search: thesearch,
            fromDate: fromValue,
            toDate: toValue
          }, function(data) {
              var table = $.makeTable(data,true);
              $("#salecontainer").html(table);
          });
      }else{
        var fromValue = $('.fromdate').val();
        var toValue = $('.todate').val();
        $('#salecontainer').empty();
        var thesearch = $('#searchsalein').val();
        $.getJSON($SCRIPT_ROOT + '/datesale' + thelist, {
          search: thesearch,
          fromDate: fromValue,
          toDate: toValue
        }, function(data) {
            var table = $.makeTable(data,true);
            $("#salecontainer").html(table);
        });
      }
  });
  /*
    * Calls for lists by vendor or subvendor
    */
  $('.vendorList').on('change', function() {
      var thelist = $('.vendorList').val();
      if(thelist === 'ech'){
      }else{
        $('#vendorcontainer').empty();
          $.getJSON($SCRIPT_ROOT + '/listvendorarea', {
          vlist: thelist
        }, function(data) {
            var table = $.makeTable(data);
            $("#vendorcontainer").html(table);
        });
      }
  });

  $('.subvendorList').on('change', function() {
      var thelist = $('.subvendorList').val();
      if(thelist === 'ech'){
      }else{
        $('#vendorcontainer').empty();
          $.getJSON($SCRIPT_ROOT + '/listsubvendorarea', {
          svlist: thelist
        }, function(data) {
            var table = $.makeTable(data);
            $("#vendorcontainer").html(table);
        });
      }
  });

  $('.ssourcelist').on('change', function() {
    var thelist = $('.ssourcelist option:selected').text();
    if(thelist === 'ech'){
    }else{
        $('#searchcontainer').empty();
        $.getJSON($SCRIPT_ROOT + '/sourceselect', {
          source: thelist
        }, function(data) {
            var table = $.makeTable(data);
            $("#searchcontainer").html(table);
        });
    }
  });
});

$('#export').click(function() {
    var titles = [];
    var data = [];
    var datat = $(this).attr("class");
    //var dataname = $(this).attr('name');
  /*
    * Get the table headers, this will be CSV headers
    * The count of headers will be CSV string separator
    */
    $( '#' + datat +  ' th').each(function(index, element) {
      if($(this).text()!=='Action'){
        titles.push($(this).text());
      }
    });

    /*
    * Get the actual data, this will contain all the data, in 1 array
    */
    $('#' + datat + ' td').each(function() {
      var correctText = $(this).text().replace(/,/g, '');
      if(correctText!=='Action'){
        data.push(correctText);
      }
    });
    
    /*
    * Convert our data to CSV string
    */
    var CSVString = prepCSVRow(titles, titles.length, '');
    CSVString = prepCSVRow(data, titles.length, CSVString);

    var downloadLink = document.createElement("a");
    var blob = new Blob(["\ufeff", CSVString]);
    var url = URL.createObjectURL(blob);
    downloadLink.href = url;
    downloadLink.download = "data.csv";

    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
});

$.makeTable = function (mydata, isSale=false) {
    var table = $('<table class="table table-striped" >');
    var tblHeader = "<tr scope='row'>";
    for (var k in mydata[0]){ if(k!=='lead_id'){tblHeader += "<th scope='col'>" + k + "</th>"}};
      if(isSale==false){
        tblHeader += "<th scope='col'>Action</th></tr>";
      }
    $(tblHeader).appendTo(table);
    $.each(mydata, function (index, value) {
        var TableRow = "<tr scope='row'>";
        var leadid = '';
        $.each(value, function (key, val) {
          if(key!=='lead_id'){
            TableRow += "<td>" + val + "</td>";
          }else{
            leadid = val;
          }
        });
        if(isSale==false){
          TableRow += "<td><button type='input' class='editbutton' id='"+ leadid +"'>Action</button></td>"
        }
        TableRow += "</tr>";
        $(table).append(TableRow);
    });
    return ($(table));
};

$(document).on('click', '.editbutton', function(e) {
      var iteminfo = [];
      var html;
      var leadid = $(this).attr("id");
      var $row = $(this).closest("tr"),       // Finds the closest row <tr> 
      $tds = $row.find("td");             // Finds all children <td> elements
      for(i = 1; i < $tds.length-1; i++){
         iteminfo.push($tds[i].textContent);
      }

      html ="<h4 align='center'>Input Sale</h4><div id='modalblock'><form id='insale'><strong>Name:<input type='text' name='name' value='" + iteminfo[2] + "' /><br/>" +
            "Policy Name:<input type='text' name='policy' /><br/>Agent:<input type='text' name='agent' /><br/>" +
            "Customer Price:<input type='text' name='price' /><br/>Down Deposit:<input type='text' name='deposit' /><br/>" +
            "Term:<input type='text' name='Term' /><br/>Source:<input type='text' name='source' value='"+ iteminfo[9] +"' /><br/>" +
            "Notes(Manual In/Out):<input type='text' name='notes' /><br/>Secondary Notes:<input type='text' name='secnotes' /><br/>" +
            "Date:<input type='text' name='date' value='"+ iteminfo[8].substring(0,10) +"' /><br/>Is Teledripped:</strong><input type='checkbox' name='istele'></form></div>";


  $('.editcontent').empty().html(html);    
  $('#editModal').toggle();

    $(document).on('click', '.btn-success', function(e) {
      var form = $('#insale').serializeArray();
      form[0]= leadid;
      form[1]= form[1].value;
      form[2]= form[2].value;
      form[3]= form[3].value;
      form[4]= form[4].value;
      form[5]= form[5].value;
      form[6]= form[6].value;
      form[7]= form[7].value;
      form[8]= form[8].value;
      form[9]= form[9].value;
      if(typeof form[10] === 'undefined') {
        // does not exist
        form[10] = '0';
      }
      else {
        // does exist
        form[10]= '1';
      }
      console.dir(form);
      $.getJSON($SCRIPT_ROOT + '/insertsale', {
        saleinfo: form
      }, function(data) {
          console.dir(data);
          if(data==true){
            alert('Success! Reloading page.');
            location.reload();
          }else{
            alert('There was an error. Please Try again.');

          }
      });
   });
});

$(document).on('click', '.btn-info', function(e) {
    $('#editModal').toggle();
});

function add(accumulator, a) {
  return parseInt(accumulator) + parseInt(a);
}
/*
* Convert data array to CSV string
* return {String} - ready CSV string
*/
function prepCSVRow(arr, columnCount, initial) {
  var row = ''; // this will hold data
  var delimeter = ','; // data slice separator
  var newLine = '\r\n'; // newline separator for CSV row

  /*
   * Convert [1,2,3,4] into [[1,2], [3,4]] while count is 2
   */
  function splitArray(_arr, _count) {
    var splitted = [];
    var result = [];
    _arr.forEach(function(item, idx) {
      if ((idx + 1) % _count === 0) {
        splitted.push(item);
        result.push(splitted);
        splitted = [];
      } else {
        splitted.push(item);
      }
    });
    return result;
  }
  var plainArr = splitArray(arr, columnCount);
  // it converts `['a', 'b', 'c']` to `a,b,c` string
  plainArr.forEach(function(arrItem) {
    arrItem.forEach(function(item, idx) {
      row += item + ((idx + 1) === arrItem.length ? '' : delimeter);
    });
    row += newLine;
  });
  return initial + row;
}
// =============== VALIDATION REGEX =============== //
const regexLetters = /^([a-zA-Z]+(_[a-zA-Z]+)*)(\s([a-zA-Z]+(_[a-zA-Z]+)*))*$/,
  regexNumbers = /^(?=.*\d)[\d ]+$/,
  regexLettersNumbers = /^[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*$/,
  regexCvv = /^[0-9]*$/;