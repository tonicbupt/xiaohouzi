$(document).ready(function () {
  bsCustomFileInput.init();
});

var form = $('form.form-upload');
var header = $('h1.h3')

function downloadFile(data, fileName) {
  var blob = new Blob([data]);
  var url = window.URL.createObjectURL(blob);
  if ('download' in document.createElement('a')) {
    // 非IE下载
    let down = document.createElement('a');
    down.href = url;
    down.download = fileName;
    document.body.append(down);
    down.click();
    window.URL.revokeObjectURL(url);
  } else {
    // IE10+下载
    navigator.msSaveBlob(blob, fileName);
  }
}

form.on('drag dragstart dragend dragover dragenter dragleave drop', function(e) {
  e.preventDefault();
  e.stopPropagation();
});

form.on('dragover dragenter', function() {
  header.html('Drop to process');
});

form.on('dragleave dragend drop', function() {
  header.html('Drag in or choose');
});

form.on('drop', function(e) {
  var file = e.originalEvent.dataTransfer.files[0];
  var formData = new FormData();
  formData.append('file', file, file.name);
  $.ajax({
    url: '/upload',
    type: 'POST',
    data: formData,
    cache: false,
    processData: false,
    contentType: false,
    xhrFields: {
      responseType: 'blob',
    },
    success: function (blob, status, xhr) {
      var name = xhr.getResponseHeader('Content-Disposition').split('filename=')[1].split(';')[0];
      downloadFile(blob, name);
    },
    error: function (data) {
      alert('error');
    }
  });
});
