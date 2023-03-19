

class API{

    constructor(infix){
        this.infix = infix
        this.KEY = 'jwt';
        this.token = localStorage.getItem(this.KEY);
        this.headers = {'Authorization': `Bearer ${this.token}`,"Content-Type": "application/json"}
        this.base_url  = `/api/v1/admin/${this.infix}`
        
        this.sufix = this.capitalize(this.infix)
        this.modalEdit = `modalEdit${this.sufix}`
        this.modalAdd = `modalAdd${this.sufix}`
        this.formAdd = `form${this.sufix}Add`
    }

    capitalize(string){
        let result = '';
        let strings = string.split('/')
        for (let str of strings){
            result += str.charAt(0).toUpperCase()+str.slice(1);
        }
        return result
    }
    async messageError(){
        return Swal.fire({title:'Algo deu errado!', icon:'error'})

    }

    async hideModal(idModal){
       return bootstrap.Modal.getInstance( document.getElementById(idModal)).hide(); 

    } 
    async showModal(idModal){
       return new bootstrap.Modal( document.getElementById(idModal),{backdrop: true}).show();

    }

    async showModalAdd(){

        document.getElementById(this.formAdd).reset()
        this.showModal(this.modalAdd)
    }

    async showModalEdit(data){
        try{data = JSON.parse(data);}catch{}
        var send = {};

        this.showModal(this.modalEdit);
        for(let key in data){
            let row = data[key]
            if (row === true || row ===false){row=Number(row)}
            let elm =  $(`#${key}_edit`)
            if (elm.length >=1){elm.val(row);send[key] = `#${key}_edit`;}
        }

        return send
    }

    async edit(data){
        this.checkTokenExists()
        try {
            let result = {}
            for(let key in data){result[key]=$(data[key]).val()}

            let req = await fetch(`${this.base_url}/edit`, {
                method: 'PUT',
                headers: this.headers,
                body:JSON.stringify(result)
            });

            let json = await req.json();
            this.parseData(req.status)



            Swal.fire(json).then(()=> {
                if (json.icon == "success"){
                    this.hideModal(this.modalEdit)
                    location.reload();
                }
            });

    } catch(error){ 
        return this.messageError()}
    }

    async delete(idRow){
        this.checkTokenExists()

        let result = await Swal.fire({
            title: 'Tem certeza que deseja deletar este item?',
            showDenyButton: true,
            showCancelButton: false,
            confirmButtonText: 'Continuar',
            denyButtonText: `Cancelar`,
            confirmButtonColor:"#05c97a"
          })
    
        if (result.isConfirmed) {
       
            try {
                let req = await fetch(`${this.base_url}/delete/${idRow}`, {
                    method: 'DELETE',
                    headers: this.headers});
        
                let json = await req.json();
                this.parseData(req.status)


                
                return Swal.fire(json).then( location.reload())

            } catch (e) {return this.messageError()}
            
        } else if (result.isDenied) {
            return Swal.fire({title:'Operação cancelada com sucesso!', icon:'info',timer:2500})
        }
    }

    async add(class_name='data'){
        this.checkTokenExists()

        try {
            let result = {}
            let elms = document.getElementsByClassName(class_name)
            if (elms){
                for(let elm of elms){
                    if (elm.localName == "input" && elm.type!="checkbox" 
                        || elm.localName == "select"){
                        result[elm.id.replace('_add','')]=$(`#${elm.id}`).val()}

                    else if (elm.localName == "input" && elm.type == "checkbox"){
                        result[elm.id.replace('_add','')] = elm.checked}
                }
            }


            let req = await fetch(`${this.base_url}/add`, {
                method: 'POST',
                headers: this.headers,
                body:JSON.stringify(result)
            });
    
            let json = await req.json();
            this.parseData(req.status)


            return Swal.fire(json).then(result =>{if (result.isConfirmed){
                    this.hideModal(this.modalAdd);
                    location.reload();
                }})

        } catch(error){
            return this.messageError()}
    }


    async filter(){
        this.checkTokenExists()

        try {

            let req = await fetch(`${this.base_url}/filter`, {
                method: 'POST',
                headers: this.headers,
                body:JSON.stringify({
                    cpf:document.getElementById('search-cpf').value.replace(/[^0-9]/g, ''),
                    pin:document.getElementById('search-id').value,
                    filter_by:$('#select-filter').val(),
                    order_by:$('#order-filter').val()
                })
            });
    
            let json = await req.json();
            this.parseData(req.status)

            return json

        } catch(error){
            return this.messageError()}
    }


    async parseData(status){
        if (status == 401){
            return Swal.fire({title:'Sua sessão expirou!',text:"Redirecionando para a página de login.", 
                        icon:'info',timer:2500}).then(
                ()=>{
                    localStorage.removeItem(this.KEY)
                    window.location.href = '/';
                }
            )
        }





    }


    async auth(email,password){
        
        try {
            let req = await fetch(this.base_url, {
                method: 'POST',
                headers:{"Content-Type": "application/json"},
                body:JSON.stringify({email,password})
            });
    
            this.parseData(req.status)

            let json = await req.json()

            if(!json.access_token){
                return Swal.fire(json)
            }

            localStorage.setItem(this.KEY,json.access_token)
            return Swal.fire(json.message).then(()=>{window.location="/admin/dashboard/home"})
    
        } catch (e) {
            return this.messageError()
        }
    }


    async checkTokenExists(){
        this.token = localStorage.getItem(this.KEY )

        if (!this.token) {
            localStorage.removeItem(this.KEY )
            window.location.href = '/';
            return }

    }

    async checkToken() {
        this.checkTokenExists()

        try {
            let req = await fetch(`/auth/validate`, {
                method: 'GET',
                headers: this.headers
            });
    
            this.parseData(req.status)
    
        } catch (e) {
            return this.messageError()
        }
    };
}


// new API("in").checkToken()