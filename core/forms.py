from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(widget=forms.Textarea, label='Mensagem')

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'nome: {nome}\nemail: {email}\nassunto: {assunto}\nmensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='claudiog.vargas@outlook.com',
            to=['claudiog.vargas@outlook.com'],
            headers={'Replay-To': email},
        )
        mail.send()
