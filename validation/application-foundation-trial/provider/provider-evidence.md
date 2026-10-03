# Bounded provider evidence

Official source inspected 2026-10-03:
https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert

The endpoint is POST /v1/sound-generation. It takes a required text field and
optional duration_seconds, model_id and output_format choices. A successful
response contains generated audio; the reference describes an MP3 result.
These facts support a direct-response operation in this paper trace.

This inspection did not establish idempotency, a durable generation job ID,
lookup after a lost response, cancellation or recovery of a lost audio response.
Treat those capabilities as unverified. Pricing, account entitlements and data
terms were not assessed. No authenticated request was made.

Use this supplied, dated evidence in the offline design trial. Additional provider
facts require later official verification; do not infer capabilities from other
endpoints or services.
