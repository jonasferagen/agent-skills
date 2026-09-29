---
name: jonas-email-style
description: "Write email in Jonas's own voice. Use when drafting, rewriting or shortening an email that Jonas will send - in Norwegian (his default) or English - so the draft sounds like him rather than like an assistant."
metadata:
  version: "0.1.0"
---

# Jonas’s email style

Derived from Jonas's own sent mail: the last 100 messages sent before 2026-09-18
(about 55 of those carry real prose - the rest are receipt forwards to the
accounting inbox and links he mails to himself), plus a sample of 17 older
English messages, since the recent window is almost entirely Norwegian.

Counterparties in that corpus: a housing co-op board colleague, the OBOS
property manager, a course-portal vendor, IT contacts at a former client,
webshops and tradesmen, and English-language consultancy/dev contacts.

## The one rule

He writes short and he writes fast. Most messages are one to six lines. He
does not introduce, does not summarize what he is about to say, and does not
close with a paragraph about looking forward to hearing back. If a draft is
longer than the facts require, it is wrong - cut lines, don't compress them
into denser sentences.

---

## Norwegian (his default)

**Greeting.** `Hei,` or `Hei!` on a new message; `Hei <Fornavn>,` when he
knows them. On a reply inside a running thread, usually no greeting at all -
he just starts. Re-contacting after a pause: `Hei igjen!` or `Hei, Lenge siden.`

**Body.** Bokmål, informal, with a-endings: *feilmeldinga, sida, stekinga,
avgrensninga*. Heavy use of the small Norwegian filler particles - *jo, vel,
da, egentlig, kanskje* - which is most of what makes him sound like himself:
"Ja den skal jo det", "det er vel greit å teste", "det burde ikke være noe
stort problem".

Abbreviations he actually uses: *spm, dvs, osv, ca, ang., pkt, hhv, eks.*
Nonstandard spellings he uses consistently and that should be left alone:
*i allefall / ihvertfall, isåfall, littegrann*.

**Asking.** He states what he already believes, then asks for confirmation
rather than asking open questions: "Er det bare å melde inn dette til X, be om
å få flytta skilt?", "Kan jeg bare si at vi gjør dette slik fra og med nå?
(Eller trengs det styrevedtak?)". Several questions get stacked as a short list
under a lead-in like `Par spm:` or as `*` / `-` bullets of one line each.

**Closing.** `Mvh` + `Jonas` is the default. `Jonas` alone on quick replies.
Full `Mvh / Jonas Feragen` plus role or address when it is a first contact or
anything official ("Vara styremedlem, Kirsebærtunet borettslag"). Short replies
inside a thread often have no sign-off at all.

**Thanks.** Warm, immediate, one line: "Mange takk for oppfølging!", "Ok takk
for snarlig svar.", "Supert, takk for så snar respons og hjelp!", "Takk for det!"

**Nagging.** He apologises for chasing before he chases: "Beklager maset.",
"Beklager maset, siste spørsmål før helga:".

**Complaining.** Credit first, then the objection stated plainly, never sharply:
"Vi setter selvsagt stor pris på at dere foretar dere det praktiske! Men det er
vel ganske skremmende at vi ikke har mulighet til å se fakturaer..."

## English

Same person, fewer particles. Plainer and slightly more clipped, because the
Norwegian hedging machinery isn't available - the hedging moves to *probably,
it seems that, hopefully, I'm afraid, I'm not sure*.

**Greeting.** `Hi,` / `Hello!` / `Hi there, and thanks for reaching out.`

**Closing.** `Jonas` alone, or `Regards,` + `Jonas`. Often the last line is the
thanks itself and there is no sign-off: "Thanks for your help so far!"

**Registers.** With devs and technical contacts: symptom first, then a
hypothesis as a question - "Lots of complaints the last few days. Could there be
any stale pods/containers that have been running for a very long time?" With
recruiters and consultancy contacts: brisk and agreeable, terms accepted in a
handful of words - "125 EUR is sufficient.", "80 EUR per hour confirmed :-)",
"Sounds interesting! You can reach me at +47 ...".

**Understating.** "It is probably not that exciting - but: it could probably be
a good exercise to..." And he will correct his own earlier message without
ceremony: "Im not sure if it is an issue after all."

**Declining.** He says what he doesn't know rather than padding: "I'm afraid I
dont have much insight in the markets."

**Giving instructions** to developers: flat imperative, then one caution, then a
smiley - "Merged the pr. Please deploy to prod. Still, look out for any 500
errors :)"

**Owning a mistake** without apology theatre: "A small issue is that all.map.js
will now be out of sync, and I should've thought about that."

**Warmth at the end of something.** When a relationship or a tool is ending he
gets noticeably more generous and slightly formal: "WS has otherwise been a
truly excellent tool... So I thank you for this. And we might definitely meet
again."

**Lowercase `i`** for "I" shows up in longer, faster English messages ("i had to
move the file", "at some point i gave up"). Leave it if it is already there;
don't add it on purpose.

---

## Mechanics that carry across both languages

- **Trailing `..`** instead of a full stop, to trail off, soften, or drop a
  thought entirely ("I should probably have filed a bug report, but.."): "det er
  ingenting å oppdrive i styrerommet i allefall..", "Snart to måneder har vært
  litt lenge å vente..", "expired Fontawesome license.. So, icons didnt render".
  This is his most recognisable tic. Use it, but once or twice per message.
- **Space before `?` and `!`**: "Testa du reboot ?", "Gratulerer med ny jobb !",
  "Skal jeg gjøre noe ? :)" - inconsistent, so not in every message.
- **English words dropped into Norwegian sentences**: *No worries., I see., Got
  it, takk!, Anyway,, Nice., Super,, Yes,, Alright., BTW, that is.* Keep these.
- **Emoticons, not emoji**: `:)` most often, `:p` and `:-)` and `:/` occasionally.
  A 👍 appears once in the whole corpus. Never more than one per message.
- **Parentheses for asides**, constantly: "(hint: sjekk spam/søppelpost)",
  "(Leilighet 5001)", "(especially on mobile where they didnt have a text
  fallback..)".
- **Emphasis** with `*asterisks*`, rarely: "*that* did cause problems for sure."
- **Spaced hyphen `-`**, never an em dash.
- **Typos stay.** He does not proofread: *dont, didnt, couldnt, Im, Barer lurte*.
  Don't imitate errors deliberately, but don't polish a draft into something
  more correct than he would have sent.
- **Plain text.** No headings, no bold, no numbered lists. Bullets are `*` or
  `-` with a fragment after them, not full sentences.

## Don't

- Don't open with "I hope this email finds you well" or any variant.
- Don't write a closing paragraph ("Please let me know if you have any
  questions" / "Ser frem til å høre fra deg"). He ends on the question itself,
  or on thanks.
- Don't stack qualifiers into long polite sentences. His politeness is one
  short warm line, then the substance.
- Don't use em dashes, bold, or markdown headings.
- Don't turn his list of three quick questions into prose.

## Templates

New ask, Norwegian:

```
Hei,

<the situation in one or two lines>

<the question, with his guess at the answer in it>

Mvh
Jonas
```

Reply inside a thread, Norwegian:

```
Ok, takk for svar. <what he'll do next, one line>
<optional second thing, opened with "Men," or "For øvrig">
```

New ask, English:

```
Hi,

<symptom or fact, one or two lines>
<hypothesis phrased as a question?>

Jonas
```
