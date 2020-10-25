$(document).ready(function() {
    $('input[type="file"]').change(function(e) {
        var fileName = e.target.files[0].name;
        $("#input-file-name").text("File selected: " + fileName);
    });

    $('input[type="file"]').change(function() {
        var ext = this.value.match(/\.(.+)$/)[1];
        switch (ext) {
            case 'flac':
                $('#summarize').attr('disabled', false);
                break;
            default:
                alert('This is not an allowed file type.');
                $('#input-file-name').text("");
                this.value = '';
        }
    });

    $('input[type="number"]').change(function() {
        var perc = this.value;
        if(perc < 0 || perc > 100) {
            alert("Not a valid percentage")
        }
    })
});