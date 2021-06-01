<template>
  <modal :show.sync="active" footerClasses="justify-content-center" type="notice">
    <h5 slot="header" class="modal-title">Record#{{ data.id }}: {{ data.name }}</h5>
    <div class="row" v-for="(record, index) in records" :key="index">
      <div class="col-4" style="font-weight:bold;">{{ record[0] }}</div>
      <div class="col-8">{{ record[1] }}</div>
    </div>
    <div slot="footer" class="justify-content-center">
      <base-button type="primary" round @click.native="active = false">Close</base-button>
    </div>
  </modal>
</template>
<script>
import { Modal } from '@/components'
export default {
  name: 'ModalView',
  components: {
    Modal
  },
  data() {
    return {
      active: false,
      data: {}
    }
  },
  computed: {
    records() {
      return [
        ['Name', this.data.name],
        ['ID', this.data.code_id],
        ['Hospital', this.data.hospital],
        ['Gender', this.data.gender],
        ['Birth Date', this.data.birth_date],
        ['Education', this.data.education],
        ['Payment', this.data.payment],
        ['Primary Kidney Disease', this.data.primary_kidney_disease],
        ['DM Status', this.data.dm_status],
        ['PD Initiation Date', this.data.pd_initiation_date],
        ['Dropout Date', this.data.dropout_date],
        ['Dropout Category', this.data.dropout_category],
        ['Dropout Cause', this.data.dropout_cause],
        ['Remarks', this.data.remarks]
      ]
    }
  }
}
</script>
<style></style>
