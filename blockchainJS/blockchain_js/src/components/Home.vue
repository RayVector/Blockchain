<template>
  <div class="row w-100 mx-auto">
    <div class="col-6 mx-auto">
      <b-form class="row mx-auto mb-2" @submit="addNewBlock">
        <b-form-group id="input-group-2" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.name"
            required
            placeholder="Enter name"
          ></b-form-input>
        </b-form-group>
        <b-button class="ml-3 h-25" type="submit" variant="primary" v-show="form.name">Write</b-button>
      </b-form>
      <b-card
        v-for="item in blocksData.chain"
        class="mb-4 w-100"
        header="Form Data Result"
        :footer="item.index"
        :key="item.index"
      >
        <pre class="m-0 w-100">{{item}}</pre>
      </b-card>
    </div>
    <div class="col-4 mx-auto">
      <b-button variant="info" @click="checkBlockchain">GET INFO</b-button>
      <b-card class="mt-4" header="Form Data Result" v-show="isCheckShow">
        <pre class="m-0">{{ validity }}</pre>
      </b-card>
    </div>
  </div>
</template>

<script>
  import Blockchain, {Block} from '../blockchain/Blockchain'

  export default {
    name: "Home",
    data() {
      return {
        jsChain: new Blockchain(),
        form: {
          name: '',
          timestamp: ''
        },
        isBlockchainShow: false,
        isCheckShow: false,
        blocksData: 'empty',
        validity: ''
      }
    },
    methods: {
      addNewBlock(e) {
        e.preventDefault();
        this.isBlockchainShow = true;
        this.form.timestamp = new Date().yyyymmdd();
        this.jsChain.addBlock(new Block(this.form.timestamp, {name: this.form.name}));
        this.form.name = '';
        this.form.timestamp = '';

        this.blocksData = this.jsChain;
        // this.blocksData = JSON.stringify(this.jsChain, null, 4);
      },
      checkBlockchain() {
        this.isCheckShow = true;
        if (this.jsChain.checkValid()) {
          this.validity = "Status: System Valid.";
        } else {
          this.validity = "Status: System Damaged.";
        }
      }
    }
  }
</script>

<style lang="stylus" scoped>

</style>