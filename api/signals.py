from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Request, Company
from django.core.mail import send_mail
from django.urls import reverse
from lokalshoppen.settings import DOMAIN_NAME


@receiver(post_save, sender=Request)
def send_confirmation(sender, instance, created, **kwargs):
    #
    # MAIL SENDING
    #
    if not created:
        # send confirmation mail to buyer if accepted
        send_mail(
            'Ihre Bestellung wurde akzeptiert',
            f"""
            Hallo,

            ihre Bestellung wurde von dem Laden akzeptiert und sie sollten in Kürze eine Rechnung durch PayPal empfangen.
            Bitte bezahlen Sie diese vor dem Abholtermin.

            Vielen Dank,
            Das Bleib Lokal! Team
            """,
            "bot@sandbox057220bc5f0c4c72bdd948cdc6745604.mailgun.org",
            [instance.customer_email],
            fail_silently=True
        )

        return

    # zum laden
    send_mail(
        'Neue Abhol-Anfrage',
        f"""
        Hallo,
        
        es ist gerade eine Abhol Anfrage von {instance.customer_email} eingegangen.
        Der Kunde möchte folgenden Artikel am tt.mm.yy zwischen hh:mm und hh:mm abholen:
        {instance.text}

        Wenn Sie diese akzeptieren wollen, schicken sie bitte eine PayPal Rechnung an den Kunden, und klicken auf folgenden Link:
        {DOMAIN_NAME + reverse('confirm', args=(instance.pk,))}
        
        Wie sende ich eine PayPal-Rechnung? 
        1. Loggen Sie sich unter https://paypal.de/login in Ihren Account ein.
        2. Klicken Sie auf Tools > Geld anfordern
        3. Tragen Sie die E-Mail-Adresse {instance.customer_email} ein und klicken auf "Weiter".
        4. Tragen Sie den Endbetrag ein, den der Kunde zu zahlen hat. 
        5. Sie können optional auch eine Mitteilung an den Kunden eintragen, beispielsweise eine Abholnummer.
        6. Klicken Sie auf "Geld anfordern"
        
        Sobald der Kunde die Bezahlung durchgeführt hat, erhalten Sie eine Bestätigung von PayPal und können dem Kunden die Bestellung im gewählten Zeitfenster bereitstellen.
        
        Vielen Dank,
        Das Bleib Lokal! Team
        """,
        "bot@sandbox057220bc5f0c4c72bdd948cdc6745604.mailgun.org",
        [instance.company.email],
        fail_silently=True
    )

    # zum kunden
    send_mail(
        'Bestätigung der Anfrage',
        f"""
        Hallo,

        ihre Bestellung ist bei uns eingegangen. Wenn der Laden ihre Bestellung akzeptiert, werden sie eine weitere E-Mail bekommen und eine Rechnung vom Laden.
        Bitte bezahlen sie die PayPal-Rechnung vor dem Abholtermin, um eine kontaktlose Übergabe zu gewährleisten.

        Vielen Dank,
        Das Bleib Lokal! Team
        """,
        "bot@sandbox057220bc5f0c4c72bdd948cdc6745604.mailgun.org",
        [instance.customer_email],
        fail_silently=True
    )