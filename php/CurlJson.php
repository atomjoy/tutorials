<?php

namespace App\Curl;

class CurlJson
{
	static function post(array $data, $url, $secure = true)
	{
		$cookie = '/tmp/curl_cookie.txt';
		$data = json_encode($data);
		$c = curl_init($url);
		curl_setopt($c, CURLOPT_CUSTOMREQUEST, "POST");
		curl_setopt($c, CURLOPT_POSTFIELDS, $data);
		curl_setopt($c, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($c, CURLOPT_HTTPHEADER, array(
			'Content-Type: application/json',
			'Content-Length: ' . strlen($data)),
      			'Accept: application/json'
		);
		curl_setopt($c, CURLOPT_SSL_VERIFYHOST,$secure);
		curl_setopt($c, CURLOPT_SSL_VERIFYPEER,$secure);
		curl_setopt($c, CURLOPT_COOKIEJAR, $cookie);
		curl_setopt($c, CURLOPT_COOKIEFILE, $cookie);
		$res = curl_exec($c);
		self::error($c, $res);
		return $res;
	}

	static function get(array $data, $url, $secure = true)
	{
		$cookie = '/tmp/curl_cookie.txt';
		$c = curl_init($url.'?'.http_build_query($data));
		curl_setopt($c, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($c, CURLOPT_SSL_VERIFYHOST,$secure);
		curl_setopt($c, CURLOPT_SSL_VERIFYPEER,$secure);
		curl_setopt($c, CURLOPT_COOKIEJAR, $cookie);
		curl_setopt($c, CURLOPT_COOKIEFILE, $cookie);
    		curl_setopt($c, CURLOPT_HTTPHEADER, array(
      			'Accept: application/json'
		);
		$res = curl_exec($c);
		self::error($c, $res);
		return $res;
	}

	static function error($c, $res)
	{
		// Curl error
		if (curl_errno($c)) {
			$msg = curl_error($c);
			throw new \Exception(curl_error($c), curl_errno($c));
		} else {
			$msg = 'Unknown error';
			$code = curl_getinfo($c, CURLINFO_HTTP_CODE);

			if($code > 400) {
				$arr = json_decode($res,true);
				$msg = $arr['message'] ?? 'Unknown message!';
				throw new \Exception($msg, $code);
			}
		}
	}
}
