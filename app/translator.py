# -*- coding: utf-8 -*-

class Translator():
    def __init__(self):
        self.strings = {
            'EN': {
                # Header
                'header1': 'Ann Helen and Stephen',
                'header2': 'have the pleasure of inviting',
                'header3': 'to their wedding, Saturday August 11th. 2018',
                'header4': 'in Dale Church in Luster, Sogn og Fjordane, 1:00 pm.',
                'header5': 'The reception will be held at Tørvis Hotel from 4:30 pm. We hope you will be able to celebrate our day with us!',

                # Program
                'program_header': 'PROGRAM',
                'program_body_1': '1:00 pm - Wedding Ceremony in Dale Church in Luster.',
                'program_body_2': '4:30 pm - Welcome drink at Tørvis Hotel, Marifjøra. Photography session.',
                'program_body_3': '5:30 pm - Dinner.',
                'program_body_4': '9:00 pm - Party, cake and fun.',
                'program_body_5': '12:30 pm - Late night snack.',

                # Wedding
                'wedding_header': 'THE WEDDING CEREMONY',
                'wedding_body': 'Dale Church is in Luster municipality in Sogn og Fjordane county, approximately 40 minutes to drive from downtown Sogndal. The stone church is from the first half of the 13th century, with interior from several different eras including the Renaissance and the Baroque.',

                # Reception
                'reception_header': 'RECEPTION',
                'reception_body_1': 'Tørvis Hotel is in Marifjøra, about 20 minutes from downtown Sogndal on the way to the church. The hotel itself has its roots from the middle of the 17th century.',
                'reception_body_2': 'William is the toastmaster for the evening. If you would like to give a speech during the reception, send him an email at wmorris@live.no. If you would rather have him relay a message from you to the newlyweds, tweet @bestmansays',

                # Accomodation
                'accomodation_header': 'ACCOMODATION',
                'accomodation_body': 'We are glad to help you with accomodations and we have reserved rooms at Tørvis from Friday the 10th. Send Ann Helen an email at annhelen@bokvennen.no if you would like to make use of the reservation.',

                # Gifts
                'gifts_header': 'GIFTS',
                'gifts_body': 'We are less concerned with gifts and more concerned with gathering friends and family for this celebration. If you would still like to give us something, we are big fans of second hand and reuse. If you have something retro/vintage you think would find a good home with us, great! Especially if the item has a story to go with it.',

                # RSVP
                'rsvp_1': 'We would love to come.',
                'rsvp_2': 'We are unable to make it.',
                'reg': 'Your registered participants:',
                'reg_answer_1': 'Thanks! We are looking forward to seeing you there!',
                'reg_answer_2': 'Please enter names and details of the people who are coming below.',
                'reg_answer_3': 'Thank you for answering. We hope to see you soon.',
                'reg_answer_4': 'Please enter an email address in case we need to reach you:',
                'reg_answer_5': 'Your registered email address:',
                'reg_answer_6': 'Change email:',

                # Register
                'reg_1': 'Given names',
                'reg_2': 'Family name',
                'reg_3': 'Allergies, if any',
                'reg_4': 'Vegan',
                'reg_5': 'Vegetarian',
                'reg_6': 'Kids Menu',
                'reg_7': 'Check boxes if applicable',
                'reg_8': 'Add participant',
                'reg_9': 'Add',

                # Contact
                'contact_0': 'CONTACT',
                'contact_1': 'Bride',
                'contact_2': 'Groom',
                'contact_3': 'Maid of honor',
                'contact_4': 'Best man',
                'contact_5': 'E-mail'
            },

            'NO': {
                # Header
                'header1': 'Ann Helen og Stephen',
                'header2': 'har gleden av å invitere',
                'header3': 'til bryllaup, laurdag 11. august 2018',
                'header4': 'i Dale kyrkje i Luster kl 13:00.',
                'header5': 'Middag og fest vil finne stad på Tørvis hotell frå kl. 16:30. Vi håpar de har moglegheit til å feire dagen med oss!',

                # Program
                'program_header': 'PROGRAM FOR DAGEN',
                'program_body_1': '13:00 - Vielse i Dale kyrkje i Luster',
                'program_body_2': '16:30 - Velkomstdrink på Tørvis hotell. Fotografering.',
                'program_body_3': '17:30 - Middag.',
                'program_body_4': '21:00 - Fest, kake og moro.',
                'program_body_5': '00:30 - Nattmat.',

                # Wedding
                'wedding_header': 'VIELSEN',
                'wedding_body': 'Dale kirke ligger i Luster kommune i Sogn og Fjordane, ca 40 minutter unna Sogndal sentrum. Steinkirken er fra første halvdel av 1200-tallet, med interiør fra forskjellige kunstepoker, bl.a. renessansen og barokken.',

                # Reception
                'reception_header': 'MIDDAG OG FEST',
                'reception_body_1': 'Tørvis hotell ligger i Marifjøra, ca. 20 minutter med bil fra Sogndal på veien til Dale kirke. Hotellet er fra rundt midten av 1600-tallet.',
                'reception_body_2': 'William vert kveldens toastmaster. Om du ynskjer å halde tale kan du ta kontakt med han på wmorris@live.no eller telefon 905 22 339. På twitterkontoen @bestmansays kan du leggje igjen ei kort helsing til brureparet om du helst vil sleppe taletid, men likevel har noko på hjartet.',

                # Accomodation
                'accomodation_header': 'OVERNATTING',
                'accomodation_body': 'Vi hjelper dykk gjerne med å finne overnatting og har reservert rom på Tørvis og Hofslund hotell frå fredag 10. august. Ta kontakt på annhelen@bokvennen.no om de ynskjer å benytte dykk av reservasjonen.',

                # Gifts
                'gifts_header': 'GAVER',
                'gifts_body': 'Vi ynskjer fyrst og fremst å samle familie og vener på dagen vår og tykkjer ikkje gåver er viktig. Om de likevel vil gje oss noko, likar vi gjenbruk og har de ein ting av retro årgang, som de tenkjer vil få eit nytt liv hjå oss, er det storarta! Elles finn de ei ynskjeliste på Kitchn sine nettsider under fana "Bryllup - finn liste". Vi ynskjer oss òg pengar til bryllaupsreise.',

                # RSVP
                'rsvp_1': 'Vi vil gjerne komme.',
                'rsvp_2': 'Vi kan dessverre ikke komme.',
                'reg': 'Dine registrerte deltakere:',
                'reg_answer_1': 'Takk for svaret! Vi gleder oss til å se deg!',
                'reg_answer_2': 'Legg til navn og detaljer om deltakerne som kommer fra dere nedenfor.',
                'reg_answer_3': 'Takk for svaret. Håper vi sees snart.',
                'reg_answer_4': 'Vennligst oppgi en epostadresse slik at vi kan nå dere:',
                'reg_answer_5': 'Din registrerte epostadresse:',
                'reg_answer_6': 'Endre din registrerte epost:',

                # Register
                'reg_1': 'Fornavn',
                'reg_2': 'Etternavn',
                'reg_3': 'Allergier, om aktuelt',
                'reg_4': 'Vegan',
                'reg_5': 'Vegetar',
                'reg_6': 'Barnemeny',
                'reg_7': 'Kryss av om',
                'reg_8': 'Legg til deltaker',
                'reg_9': 'Legg til',

                # Contact
                'contact_0': 'KONTAKT',
                'contact_1': 'Brud',
                'contact_2': 'Brudgom',
                'contact_3': 'Brudens forlover',
                'contact_4': 'Brudgoms forlover',
                'contact_5': 'E-post'
            }
        }

    def get_localized_dict(self, language):
        return self.strings[language]

    def set_localized_string(self, language, key, string):
        self.strings[language][key] = string

    def get_localized_string(self, language, key):
        return self.strings[language][key]
