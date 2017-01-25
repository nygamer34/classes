<?php
$pythonScript = '../../../python/sample_project/data_transfer.py ';
// This is the data you want to pass to Python
$data = array('value1', 'value2', 'value3');

// Execute the python script with the JSON data
$result = shell_exec('python '. $pythonScript . escapeshellarg(json_encode($data)));

// Decode the result
$resultData = json_decode($result, true);

// This will contain: array('status' => 'Yes!')
var_dump($resultData);
?>