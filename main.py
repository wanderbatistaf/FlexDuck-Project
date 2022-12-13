import gi

import model
import report_clients
from model import db
import alert_dialogs

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from controller import ControllerModelPycFile
from report_clients import ReportClients
from datetime import date

builder = Gtk.Builder()
builder.add_from_file("frm_start.glade")

today = date.today()

limite = 0

class App(ControllerModelPycFile, ReportClients):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.start_ui_clientes()
        self.cadastrado_em()
        self.create_db()

    def create_db(self, *args):
        db.create_tables([model.Usuarios])


    def start_ui_clientes(self):
        self.tb_imprimir1 = builder.get_object("tb_imprimir1")
        self.gtk_edit = builder.get_object("gtk_edit")
        self.tb_excluir1 = builder.get_object("tb_excluir1")
        self.tb_proximo1 = builder.get_object("tb_proximo1")
        self.tb_anterior1 = builder.get_object("tb_anterior1")
        self.check_pf1 = builder.get_object("check_pf1")
        self.txt_website = builder.get_object("txt_website")
        self.txt_instagram = builder.get_object("txt_instagram")
        self.check_pf1 = builder.get_object("check_pf1")
        self.txt_bairro1 = builder.get_object("txt_bairro1")
        self.txt_cidade1 = builder.get_object("txt_cidade1")
        self.cmb_uf1 = builder.get_object("cmb_uf1")
        self.txt_logradouro1 = builder.get_object("txt_logradouro1")
        self.txt_cep1 = builder.get_object("txt_cep1")
        self.btn_cep1 = builder.get_object("btn_cep1")
        self.gtk_clear = builder.get_object("gtk_clear")
        self.txt_dtbloqueado1 = builder.get_object("txt_dtbloqueado1")
        self.txt_inativodesde1 = builder.get_object("txt_inativodesde1")
        self.check_inativo1 = builder.get_object("check_inativo1")
        self.check_bloqueado1 = builder.get_object("check_bloqueado1")
        self.txt_dtcadastro1 = builder.get_object("txt_dtcadastro1")
        self.txt_codigo1 = builder.get_object("txt_codigo1")
        self.dialog_window = builder.get_object("dialog_window")
        self.txt_localizar1 = builder.get_object("txt_localizar1")
        self.txt_nome1 = builder.get_object("txt_nome1")
        self.txt_razao1 = builder.get_object("txt_razao1")
        self.txt_cnpj_cpf1 = builder.get_object("txt_cnpj_cpf1")
        self.txt_ie1 = builder.get_object("txt_ie1")
        self.txt_im1 = builder.get_object("txt_im1")
        self.txt_tel_cel = builder.get_object("txt_tel_cel")
        self.txt_tel_fixo = builder.get_object("txt_tel_fixo")
        self.txt_tel_recado = builder.get_object("txt_tel_recado")
        self.txt_email = builder.get_object("txt_email")
        self.main_window = builder.get_object("frm_start")
        self.main_window.show_all()

    #Busca data atual para o campo Data de Cadastro
    def cadastrado_em(self, *args):
        hoje = date.today().strftime("%d/%m/%Y")
        self.txt_dtcadastro1.set_text(str(hoje))

    #Destroy a Janela
    def on_frm_start_destroy(self, *args):
        Gtk.main_quit()

    def on_tb_sair_clicked(self, *args):
        Gtk.main_quit()

    def on_tb_sair_clicked1(self, *args):
        Gtk.main_quit()

    def on_tb_sair_clicked2(self, *args):
        Gtk.main_quit()

    #Renderiza o modelo de dados obtidos
    def renderer_model(self, model):
        try:
            if model:
                print(model)
                self.lst_rows.clear()
                for rows in model:
                    self.lst_rows.append(rows)
        except Exception as ex:
            print('Erro %s' % ex)

    #Clear Button
    def on_gtk_clear(self, *args):
        self.txt_codigo1.set_text(str(""))
        self.txt_nome1.set_text("")
        self.txt_razao1.set_text("")
        self.txt_cnpj_cpf1.set_text("")
        self.txt_ie1.set_text("")
        self.txt_im1.set_text("")
        self.txt_tel_cel.set_text("")
        self.txt_tel_fixo.set_text("")
        self.txt_tel_recado.set_text("")
        self.txt_email.set_text("")
        self.txt_logradouro1.set_text("")
        self.txt_bairro1.set_text("")
        self.txt_cidade1.set_text("")
        self.cmb_uf1.set_text("")
        self.txt_cep1.set_text("")
        self.txt_instagram.set_text("")
        self.txt_website.set_text("")
        self.txt_localizar1.set_text("")
        self.cadastrado_em()

        self.check_pf1.set_active(False)
        self.check_pf1.set_sensitive(True)
        self.txt_nome1.set_can_focus(True)
        self.txt_razao1.set_can_focus(True)
        self.txt_cnpj_cpf1.set_can_focus(True)
        self.txt_ie1.set_can_focus(True)
        self.txt_im1.set_can_focus(True)
        self.txt_tel_cel.set_can_focus(True)
        self.txt_tel_fixo.set_can_focus(True)
        self.txt_tel_recado.set_can_focus(True)
        self.txt_email.set_can_focus(True)
        self.txt_dtcadastro1.set_can_focus(True)
        self.txt_inativodesde1.set_can_focus(True)
        self.txt_dtbloqueado1.set_can_focus(True)
        self.txt_cep1.set_can_focus(True)
        self.txt_logradouro1.set_can_focus(True)
        self.txt_bairro1.set_can_focus(True)
        self.txt_cidade1.set_can_focus(True)
        self.cmb_uf1.set_can_focus(True)
        self.txt_tel_fixo.set_can_focus(True)
        self.txt_tel_cel.set_can_focus(True)
        self.txt_tel_recado.set_can_focus(True)
        self.txt_instagram.set_can_focus(True)
        self.txt_website.set_can_focus(True)

    #Botão Adicionar Cliente
    def on_bt_user_add_clicked(self, *args):
        try:
            dialog = alert_dialogs.AlertAdicionar(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                dialog.destroy()
                nome = self.txt_nome1.get_text()
                razaosocial = self.txt_razao1.get_text()
                cnpjcpf = self.txt_cnpj_cpf1.get_text()
                ie = self.txt_ie1.get_text()
                im = self.txt_im1.get_text()
                celular = self.txt_tel_cel.get_text()
                fixo = self.txt_tel_fixo.get_text()
                recado = self.txt_tel_recado.get_text()
                email = self.txt_email.get_text()
                created_at = self.txt_dtcadastro1.get_text()
                inactive_since = self.txt_inativodesde1.get_text()
                blocked_since = self.txt_dtbloqueado1.get_text()
                cep = self.txt_cep1.get_text()
                street = self.txt_logradouro1.get_text()
                district = self.txt_bairro1.get_text()
                city = self.txt_cidade1.get_text()
                state = self.cmb_uf1.get_text()
                telephone = self.txt_tel_fixo.get_text()
                cellphone = self.txt_tel_cel.get_text()
                errands = self.txt_tel_recado.get_text()
                instagram = self.txt_instagram.get_text()
                website = self.txt_website.get_text()
                natural_person = self.check_pf1.get_active()
                self.insert_user(nome, razaosocial, cnpjcpf, ie, im,
                                 celular, fixo, recado, email, created_at,
                                 inactive_since, blocked_since, cep, street,
                                 district, city, state, telephone, cellphone,
                                 errands, instagram, website, natural_person)
                print(f"O Usuário {nome} foi adicionado com sucesso.")
                print(f"{nome}, {razaosocial}, {cnpjcpf}, {ie}, {im},{celular}, "
                      f"{fixo}, {recado}, {email}, {created_at},{inactive_since}, "
                      f"{blocked_since}, {cep}, {street}, {district}, {city}, {state}, "
                      f"{telephone}, {cellphone}, {errands}, {instagram}, {website}, "
                      f"{natural_person}")
                self.show_dialog(self.dialog_window, "Sucess!",
                                 (f"O Usuário {nome} foi adicionado com sucesso."))
                self.on_gtk_clear()
            elif response == Gtk.ResponseType.NO:
                pass
                print("The cancel button was clicked")
            dialog.destroy()
        except Exception as ex:
            print("Error: %s \nSignal: %s \nArgs: %s" % (
                ex, "on_bt_user_add_clicked", args
                 )
            )

    #Localiza O Cliente Através da Barra Superior
    def tb_localizar1_clicked_cb(self, *args):
        try:
            localizar1 = self.txt_localizar1.get_text()
            found = self.search_user(localizar1)
            self.txt_codigo1.set_text(str(found["idcliente"]))
            self.txt_nome1.set_text(found["nome"])
            self.txt_razao1.set_text(found["razaosocial"])
            self.txt_cnpj_cpf1.set_text(found["cnpjcpf"])
            self.txt_ie1.set_text(found["ie"])
            self.txt_im1.set_text(found["im"])
            self.txt_tel_cel.set_text(found["celular"])
            self.txt_tel_fixo.set_text(found["fixo"])
            self.txt_tel_recado.set_text(found["recado"])
            self.txt_email.set_text(found["email"])
            self.txt_dtcadastro1.set_text(found["created_at"])
            self.txt_inativodesde1.set_text(found["inactive_since"])
            self.txt_dtbloqueado1.set_text(found["blocked_since"])
            self.txt_cep1.set_text(found["cep"])
            self.txt_logradouro1.set_text(found["street"])
            self.txt_bairro1.set_text(found["district"])
            self.txt_cidade1.set_text(found["city"])
            self.cmb_uf1.set_text(found["state"])
            self.txt_tel_fixo.set_text(found["telephone"])
            self.txt_tel_cel.set_text(found["cellphone"])
            self.txt_tel_recado.set_text(found["errands"])
            self.txt_instagram.set_text(found["instagram"])
            self.txt_website.set_text(found["website"])
            self.check_pf1.set_active(found["natural_person"])

        #Impedindo Alteração do User Após Pesquisa
            self.txt_codigo1.set_editable(False)
            self.txt_nome1.set_can_focus(False)
            self.txt_razao1.set_can_focus(False)
            self.txt_cnpj_cpf1.set_can_focus(False)
            self.txt_ie1.set_can_focus(False)
            self.txt_im1.set_can_focus(False)
            self.txt_tel_cel.set_can_focus(False)
            self.txt_tel_fixo.set_can_focus(False)
            self.txt_tel_recado.set_can_focus(False)
            self.txt_email.set_can_focus(False)
            self.txt_dtcadastro1.set_can_focus(False)
            self.txt_inativodesde1.set_can_focus(False)
            self.txt_dtbloqueado1.set_can_focus(False)
            self.txt_cep1.set_can_focus(False)
            self.txt_logradouro1.set_can_focus(False)
            self.txt_bairro1.set_can_focus(False)
            self.txt_cidade1.set_can_focus(False)
            self.cmb_uf1.set_can_focus(False)
            self.txt_tel_fixo.set_can_focus(False)
            self.txt_tel_cel.set_can_focus(False)
            self.txt_tel_recado.set_can_focus(False)
            self.txt_instagram.set_can_focus(False)
            self.txt_website.set_can_focus(False)
            self.check_pf1.set_sensitive(False)
        except Exception as ex:
            self.show_dialog(self.dialog_window, "Error!",
                             (f"Não foi possivel localizar o cliente: {self.txt_localizar1.get_text()}."))
            self.on_gtk_clear()

    #Botão de pesquisa ANTERIOR
    def on_tb_anterior1_clicked(self, *args):
        lb4 = self.txt_localizar1.get_text()
        if lb4 == "":
            lb4 = 2
        else:
            if lb4 != int():
                lb4 = self.txt_codigo1.get_text()
        val = int(lb4)
        if val <= limite:
            val = limite + 1
        lb4 = str(val - 1)
        self.txt_localizar1.set_text(lb4)
        self.tb_localizar1_clicked_cb()

    #Botão de pesquisa PROXIMO
    def on_tb_proximo1_clicked(self, *args):
        lb4 = self.txt_localizar1.get_text()
        if lb4 == "":
            lb4 = 1
        else:
            if lb4 == "" or lb4 != int():
                lb4 = self.txt_codigo1.get_text()
        val = int(lb4)
        lb4 = str(val + 1)
        self.txt_localizar1.set_text(lb4)
        self.tb_localizar1_clicked_cb()


    #Habilida e Desabilita o Campo de Inativo desde
    def on_check_inativo1_toggled(self, *args):
        if self.check_inativo1.get_active():
            self.txt_inativodesde1.set_sensitive(True)
        else:
            self.txt_inativodesde1.set_sensitive(False)

    #Habilida e Desabilita o Campo de Bloqueado desde
    def on_check_bloqueado1_toggled(self, *args):
        if self.check_bloqueado1.get_active():
            self.txt_dtbloqueado1.set_sensitive(True)
        else:
            self.txt_dtbloqueado1.set_sensitive(False)

    #Botão de Exclusão de Clientes
    def on_tb_excluir1_clicked(self, *args):
        try:
            dialog = alert_dialogs.AlertExcluir(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                # O que acontece se clicar no SIM
                dialog.destroy()
                idcliente = self.txt_codigo1.get_text()
                if idcliente != "":
                    deleted_user = self.delete_user(idcliente)
                    nome = self.txt_nome1.get_text()
                    print(nome)
                    print(deleted_user)
                    self.show_dialog(self.dialog_window, "Sucess!",
                                     (f"O Usuário {nome} foi excluído com sucesso."))
                    self.on_gtk_clear()
                else:
                    self.show_dialog(self.dialog_window, "Error!",
                                     (f"Não foi possivel excluir o cliente: {self.txt_nome1.get_text()}."))
                    self.on_gtk_clear()
                print("The YES button was clicked")
                # O que acontece se clicar no NÃO
            elif response == Gtk.ResponseType.NO:
                pass
                print("The Cancel button was clicked")
            dialog.destroy()
        except Exception as ex:
            self.show_dialog(self.dialog_window, "Error!",
                     (f"Não foi possivel excluir o cliente: {self.txt_nome1.get_text()}."))
            self.on_gtk_clear()

    #Botão de Editar cliente. <--ESTÁ APARECENDO 2X AO CLICAR EM NÃO-->
    def gtk_edit_toggled_cb(self, *args):
        cliente_id = self.txt_codigo1.get_text()
        print(cliente_id)
        try:
            dialog = alert_dialogs.AlertEditUserStart(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                dialog.destroy()
                print("Button YES was clicked")
            #Checa se o id do cliente é diferente de vazio
                if cliente_id != "":
                    if self.gtk_edit.get_active():
                        dialog.destroy()
                        # Liberando Alteração do User Após Pesquisa
                        self.txt_codigo1.set_editable(False)
                        self.txt_nome1.set_can_focus(True)
                        self.txt_razao1.set_can_focus(True)
                        self.txt_cnpj_cpf1.set_can_focus(True)
                        self.txt_ie1.set_can_focus(True)
                        self.txt_im1.set_can_focus(True)
                        self.txt_tel_cel.set_can_focus(True)
                        self.txt_tel_fixo.set_can_focus(True)
                        self.txt_tel_recado.set_can_focus(True)
                        self.txt_email.set_can_focus(True)
                        self.txt_dtcadastro1.set_can_focus(True)
                        self.txt_inativodesde1.set_can_focus(True)
                        self.txt_dtbloqueado1.set_can_focus(True)
                        self.txt_cep1.set_can_focus(True)
                        self.txt_logradouro1.set_can_focus(True)
                        self.txt_bairro1.set_can_focus(True)
                        self.txt_cidade1.set_can_focus(True)
                        self.cmb_uf1.set_can_focus(True)
                        self.txt_tel_fixo.set_can_focus(True)
                        self.txt_tel_cel.set_can_focus(True)
                        self.txt_tel_recado.set_can_focus(True)
                        self.txt_instagram.set_can_focus(True)
                        self.txt_website.set_can_focus(True)
                        self.check_pf1.set_sensitive(True)
                        state = "on"
                        dialog.destroy()
                    else:
                        dialog.destroy()
                        new_idcliente = self.txt_codigo1.get_text()
                        new_nome = self.txt_nome1.get_text()
                        new_razaosocial = self.txt_razao1.get_text()
                        new_cnpjcpf = self.txt_cnpj_cpf1.get_text()
                        new_ie = self.txt_ie1.get_text()
                        new_im = self.txt_im1.get_text()
                        new_celular = self.txt_tel_cel.get_text()
                        new_fixo = self.txt_tel_fixo.get_text()
                        new_recado = self.txt_tel_recado.get_text()
                        new_email = self.txt_email.get_text()
                        new_created_at = self.txt_dtcadastro1.get_text()
                        new_inactive_since = self.txt_inativodesde1.get_text()
                        new_blocked_since = self.txt_dtbloqueado1.get_text()
                        new_cep = self.txt_cep1.get_text()
                        new_street = self.txt_logradouro1.get_text()
                        new_district = self.txt_bairro1.get_text()
                        new_city = self.txt_cidade1.get_text()
                        new_state = self.cmb_uf1.get_text()
                        new_telephone = self.txt_tel_fixo.get_text()
                        new_cellphone = self.txt_tel_cel.get_text()
                        new_errands = self.txt_tel_recado.get_text()
                        new_instagram = self.txt_instagram.get_text()
                        new_website = self.txt_website.get_text()
                        new_natural_person = self.check_pf1.get_active()
                        self.update_user(new_idcliente, new_nome, new_razaosocial, new_cnpjcpf, new_ie, new_im,
                                         new_celular, new_fixo, new_recado, new_email, new_created_at,
                                         new_inactive_since, new_blocked_since, new_cep, new_street,
                                         new_district, new_city, new_state, new_telephone, new_cellphone,
                                         new_errands, new_instagram, new_website, new_natural_person)
                        dialog.destroy()
                        print(f"O Usuário {new_nome} foi alterado com sucesso.")
                        print(
                            f"{new_nome}, {new_razaosocial}, {new_cnpjcpf}, {new_ie}, {new_im},{new_celular}, {new_fixo}, "
                            f"{new_recado}, {new_email}, {new_created_at},{new_inactive_since}, {new_blocked_since}, {new_cep}, "
                            f"{new_street}, {new_district}, {new_city}, {new_state}, {new_telephone}, {new_cellphone}, {new_errands},"
                            f" {new_instagram}, {new_website}, {new_natural_person}")
                        self.show_dialog(self.dialog_window, "Sucess!",
                                         (f"O Usuário {new_nome} foi alterado com sucesso."))
                        self.on_gtk_clear()
                        state = "off"
                        print("Button", "was turned", state)
                else:
                    self.gtk_edit.set_active(False)
                    self.show_dialog(self.dialog_window, "Error!",
                    (f"Não foi possivel alterar o cliente: {self.txt_nome1.get_text()}."))
                    self.on_gtk_clear()
            elif response == Gtk.ResponseType.NO:
                print("Button NO was clicked")
                dialog.destroy()
                self.gtk_edit.set_active(False)
        except Exception as ex:
                print("Error: %s \nSignal: %s \nArgs: %s" % (
                    ex, "on_bt_user_add_clicked", args
                    )
                )


    #Localiza o CEP através da API e preenche
    def on_btn_cep1_clicked(self, *args):
        cep = self.txt_cep1.get_text()
        consult_cep = self.consuming_cep(cep)
        self.txt_logradouro1.set_text(consult_cep[0])
        self.txt_bairro1.set_text(consult_cep[1])
        self.txt_cidade1.set_text(consult_cep[2])
        self.cmb_uf1.set_text(consult_cep[3])


    #Imprimir Relatório <--CONTINUAR DAQUI-->
    def tb_imprimir1_clicked_cb(self, *args):
        try:
            dialog = alert_dialogs.AlertImprimirRelatorio(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                #O que acontece se clicar em SIM
                print("The yes button was clicked")
                filename = "ClientReport_{}.csv"
                idcliente = self.txt_codigo1.get_text()
                self.getidreport(idcliente, filename)
                dialog.destroy()
            elif response == Gtk.ResponseType.NO:
                dialog.destroy()
                print("The cancel button was clicked")

            dialog.destroy()
        except Exception as ex:
                print("Error: %s \nSignal: %s \nArgs: %s" % (
                    ex, "tb_imprimir1_clicked_cb", args
                    )
                )


    # Show Message Dialog
    def show_dialog(self, component, title, text, icon=None):
       component.props.text = (title)
       component.props.secondary_text = (text)
       component.props.icon_name = (icon)
       component.props.modal
       component.show_all()
       component.run()
       component.hide()


if __name__ == '__main__':
    builder.connect_signals(App())
    Gtk.main()