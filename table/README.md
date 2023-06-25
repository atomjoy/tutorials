# table

```html
<table>
	<tr>
		<th colspan="6" style="background-color: #f40">Table with 1, 2, 3 columns!</th>
	</tr>
	<tr>
		<td colspan="6" style="text-align:center;">Jazz</td>
	</tr>
	<tr>
		<td colspan="3" style="background-color: #07f">Jazz</td>
		<td colspan="3" style="background-color: #07f">Jazz</td>
	</tr>
	<tr>
		<td colspan="2">1</td>
		<td colspan="2">2</td>
		<td colspan="2">3</td>
	</tr>
</table>

<style>
	table {
		border-collapse: collapse;
	}

	td,
	th {
		border: 1px solid black;
		padding: 10px 20px;
	}
</style>
```

### table rowspan

```html
<table width="600">
	<tr>
		<td rowspan="4" style="background-color: #f40" width="150">Image</td>
		<td style="text-align:center;">Name</td>
	</tr>
	<tr>
		<td style="text-align:center;">Job</td>
	</tr>
	<tr>
		<td style="background-color: #07f">Email</td>
	</tr>
	<tr>
		<td style="background-color: #07f">Phone/td>
	</tr>
</table>
```

### table bg

```html
<table class="container" role="presentation" cellpadding="0" cellspacing="0" border="0" width="600">
<tr>
	<td style="
		height: 100vh;
		background: url('https://images.pexels.com/photos/794494/pexels-photo-794494.jpeg');
		background-size: cover;
		background-position: top center;
	">
		<!--add your content here-->
	</td>
</tr>
</table>
 ```
