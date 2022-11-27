<template></template>
<script>
export default {
	data() {
		return {}
	},
	watch: {
		'$i18n.locale': function (cur, old) {
			document.title = this.$t(this.title)
		},
	},
	name: 'PageTitle',
	props: {
		title: {
			type: String,
			default: 'error404.title',
		},
	},
	mounted() {
		document.title = this.$t(this.title)
	},
}
</script>
