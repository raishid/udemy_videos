<?php
    $comparar = strpos($_POST['url_udemy'], 'https://mp4-a.udemycdn.com/');
    if(isset($_POST['url_udemy']) && $comparar !== false && isset($_POST['titulo'])){
        $video = $_POST['url_udemy'];
        $headers= get_headers($video, 1);
        $filesize = $headers['Content-Length'];
        $name = $_POST['titulo'].'.mp4';
        header('Content-type: video/mp4');
        header("Content-disposition: attachment; filename=$name");
        header("Content-Length: ".$filesize);
        readfile($video);
    }else{
        ?>
        <h1>Link url incorrecta</h1>
        <?php
    }