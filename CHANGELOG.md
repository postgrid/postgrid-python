# Changelog

## 2.3.0 (2026-06-12)

Full Changelog: [v2.2.0...v2.3.0](https://github.com/postgrid/postgrid-python/compare/v2.2.0...v2.3.0)

### Features

* **api:** update api with events and webhook capabilities ([6472f0c](https://github.com/postgrid/postgrid-python/commit/6472f0c67cae5d8946f43724d29f53762178918b))
* New endpoints, fixed and aligned schemas ([c8be87f](https://github.com/postgrid/postgrid-python/commit/c8be87f4cfc054bc31b63e3dd1ab59183664801c))
* PE-6131 HOTFIX: Fix idempotency key header for create endpoints ([6d2ab69](https://github.com/postgrid/postgrid-python/commit/6d2ab69231ab511d841c2fb914159513d1c64c27))
* Update available premium paper IDs ([2791811](https://github.com/postgrid/postgrid-python/commit/27918110696bddf2afd84fc854d6a1d7ce139e9a))

## 2.2.0 (2026-05-13)

Full Changelog: [v2.1.1...v2.2.0](https://github.com/postgrid/postgrid-python/compare/v2.1.1...v2.2.0)

### Features

* **api:** Generate OpenAPI spec from master, Complete AV endpoints, Deprecate order profiles ([e077d42](https://github.com/postgrid/postgrid-python/commit/e077d42c1fa32be25d6b458d0095c4a94a008ad1))
* **api:** sheikh's updates ([bdc7fef](https://github.com/postgrid/postgrid-python/commit/bdc7fef6407b6906f7289f302a1281bc76730297))
* **internal/types:** support eagerly validating pydantic iterators ([2124510](https://github.com/postgrid/postgrid-python/commit/2124510f8373868ec16a60ffdccd6f5d47e7ad17))
* support setting headers via env ([e690d3e](https://github.com/postgrid/postgrid-python/commit/e690d3eea529e14db8ef172128b126e9c62a0bfa))
* Testing new GHA workflow ([aa4a426](https://github.com/postgrid/postgrid-python/commit/aa4a42689f6e30a8c6566ef225f198a149ceb3d6))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([459beb6](https://github.com/postgrid/postgrid-python/commit/459beb65a1c41126dd02d19cabf529c45c8e531c))
* use correct field name format for multipart file arrays ([4662cc7](https://github.com/postgrid/postgrid-python/commit/4662cc7a36251fb808df1ac04ee5bbecfeaf9ebb))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([ad870fb](https://github.com/postgrid/postgrid-python/commit/ad870fb8a30f20b4193f7eed5a96755a9a656228))


### Chores

* **internal:** more robust bootstrap script ([e3ae215](https://github.com/postgrid/postgrid-python/commit/e3ae21534f0e6048dd59631aa02c04d5c1f3a681))
* **internal:** reformat pyproject.toml ([872adb3](https://github.com/postgrid/postgrid-python/commit/872adb3468462b205c3619f1de65cf163f982ad3))

## 2.1.1 (2026-04-10)

Full Changelog: [v2.1.0...v2.1.1](https://github.com/postgrid/postgrid-python/compare/v2.1.0...v2.1.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([a88e2b2](https://github.com/postgrid/postgrid-python/commit/a88e2b213e628430a0a608c0d0df0af9f09ab2da))
* ensure file data are only sent as 1 parameter ([499ccd8](https://github.com/postgrid/postgrid-python/commit/499ccd837cacd93138b3edab75b95ebfe33742e2))

## 2.1.0 (2026-03-26)

Full Changelog: [v2.0.3...v2.1.0](https://github.com/postgrid/postgrid-python/compare/v2.0.3...v2.1.0)

### Features

* **client:** add custom JSON encoder for extended type support ([7daf14d](https://github.com/postgrid/postgrid-python/commit/7daf14d1ea87c9036961bbcc15399e90ed118cbb))
* **client:** add support for binary request streaming ([9c92b6a](https://github.com/postgrid/postgrid-python/commit/9c92b6a0f2411b015adf447dffa582836bc1ac4a))
* **internal:** implement indices array format for query and form serialization ([796fd65](https://github.com/postgrid/postgrid-python/commit/796fd65720ecce3553f7adbcef50ac1f85c14291))


### Bug Fixes

* **client:** loosen auth header validation ([af955ca](https://github.com/postgrid/postgrid-python/commit/af955ca7182b4f032d6d9c10faf060668fa43248))
* **deps:** bump minimum typing-extensions version ([aa94631](https://github.com/postgrid/postgrid-python/commit/aa94631c7c4fd65cff55b9d86263aa1926dd4f75))
* **pydantic:** do not pass `by_alias` unless set ([6f9b35c](https://github.com/postgrid/postgrid-python/commit/6f9b35c003e312b228ba36b527a09671b0700039))
* sanitize endpoint path params ([b59444c](https://github.com/postgrid/postgrid-python/commit/b59444c1ceb05ede740db7dd87eec8e2a7478de1))
* use async_to_httpx_files in patch method ([a3b137a](https://github.com/postgrid/postgrid-python/commit/a3b137ae1ab33697009d7b508a8d22f7349b9dec))


### Chores

* **ci:** skip lint on metadata-only changes ([7538d3d](https://github.com/postgrid/postgrid-python/commit/7538d3d8a3b9e34a00b9c8b4ad1db5a81224f287))
* **ci:** skip uploading artifacts on stainless-internal branches ([a64ce59](https://github.com/postgrid/postgrid-python/commit/a64ce5957d66b86e6d14bdcf4ed29eb12f5d559c))
* **ci:** upgrade `actions/github-script` ([e2ea5fd](https://github.com/postgrid/postgrid-python/commit/e2ea5fdecfc467358d53198d37f153ea7f7bf0cf))
* **docs:** add missing descriptions ([9dd7392](https://github.com/postgrid/postgrid-python/commit/9dd73922effb1185e3ef1a21cf0118f1b1319384))
* format all `api.md` files ([0a364e2](https://github.com/postgrid/postgrid-python/commit/0a364e28d4d8c4039925ead02608bcc66f6253f8))
* **internal:** add `--fix` argument to lint script ([e8d9998](https://github.com/postgrid/postgrid-python/commit/e8d9998a7bc735ebb82e4071f479b6d811746abd))
* **internal:** add missing files argument to base client ([6dbed91](https://github.com/postgrid/postgrid-python/commit/6dbed918a54c190cda4e2b7c1c8b56867bde3562))
* **internal:** add request options to SSE classes ([986b89d](https://github.com/postgrid/postgrid-python/commit/986b89d9ed6752401d1a0a2caa05a74b3fc805ff))
* **internal:** bump dependencies ([53cb8a0](https://github.com/postgrid/postgrid-python/commit/53cb8a03ab0c3d88881b7c2acdde5288f8511f7e))
* **internal:** codegen related update ([eb02a83](https://github.com/postgrid/postgrid-python/commit/eb02a837ede94d5440593cb9c921c6e47ae5a0ab))
* **internal:** fix lint error on Python 3.14 ([8a7fe14](https://github.com/postgrid/postgrid-python/commit/8a7fe146bf634f2fab49203e50eca29f43f3f1c3))
* **internal:** make `test_proxy_environment_variables` more resilient ([b33f0fb](https://github.com/postgrid/postgrid-python/commit/b33f0fb4114274c85f1c0441f17bde2de3500180))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([d60d095](https://github.com/postgrid/postgrid-python/commit/d60d09529bdcb3df50effb16c004a04c5ab76e8c))
* **internal:** remove mock server code ([961b979](https://github.com/postgrid/postgrid-python/commit/961b979236edcd88d3c3f2b03f1033940b188bd2))
* **internal:** tweak CI branches ([e723bef](https://github.com/postgrid/postgrid-python/commit/e723befd334a20b5f8b02322edfb84dd19c46337))
* **internal:** update `actions/checkout` version ([0d17288](https://github.com/postgrid/postgrid-python/commit/0d1728886ee999032574dd9877bc85c84930bc3b))
* **internal:** update gitignore ([3e89493](https://github.com/postgrid/postgrid-python/commit/3e89493903b49b783cd2157928455b1b161043f4))
* speedup initial import ([32fb2cc](https://github.com/postgrid/postgrid-python/commit/32fb2cceb7859e77a4840e4f45bc782123aa0359))
* update mock server docs ([168a3b8](https://github.com/postgrid/postgrid-python/commit/168a3b8c77755038a1fefd557d71ad49f753a360))

## 2.0.3 (2025-12-09)

Full Changelog: [v2.0.2...v2.0.3](https://github.com/postgrid/postgrid-python/compare/v2.0.2...v2.0.3)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([da4eda9](https://github.com/postgrid/postgrid-python/commit/da4eda9cfa2f8713841e9668e01efc7e2e09a420))


### Chores

* add missing docstrings ([3b3c572](https://github.com/postgrid/postgrid-python/commit/3b3c5722c15adddc6b388b05007cbc277559dc33))

## 2.0.2 (2025-12-03)

Full Changelog: [v2.0.1...v2.0.2](https://github.com/postgrid/postgrid-python/compare/v2.0.1...v2.0.2)

### Bug Fixes

* ensure streams are always closed ([c965753](https://github.com/postgrid/postgrid-python/commit/c9657539f5012e08de7808d23cec1519ce05ce97))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([258650e](https://github.com/postgrid/postgrid-python/commit/258650e3f215923b814f96d396e4baa2164fa3ca))
* **docs:** use environment variables for authentication in code snippets ([38d4794](https://github.com/postgrid/postgrid-python/commit/38d47943a7e60a9034c31845162edd1324c0b575))
* update lockfile ([eb75a19](https://github.com/postgrid/postgrid-python/commit/eb75a1991628cf5164d4c2f4fc2fff0342b50566))

## 2.0.1 (2025-11-22)

Full Changelog: [v2.0.0...v2.0.1](https://github.com/postgrid/postgrid-python/compare/v2.0.0...v2.0.1)

### Chores

* add Python 3.14 classifier and testing ([7e2917a](https://github.com/postgrid/postgrid-python/commit/7e2917a5dec82c83534abca2719438830bed406e))

## 2.0.0 (2025-11-13)

Full Changelog: [v0.0.1-alpha.0...v2.0.0](https://github.com/postgrid/postgrid-python/compare/v0.0.1-alpha.0...v2.0.0)

### Bug Fixes

* **api:** Pacify pyright ([0dea36d](https://github.com/postgrid/postgrid-python/commit/0dea36d9fcab59fec8412c753bc66b4dbc5b99e1))
* **api:** Prepare request fix ([9f737cc](https://github.com/postgrid/postgrid-python/commit/9f737cc73d70892712759f52624ade9f9bd8ba7e))
* **api:** remove unsupported collaterals ([fdbeb1a](https://github.com/postgrid/postgrid-python/commit/fdbeb1a3cf24dfbdaff4bf08966b6b04853e2840))
* compat with Python 3.14 ([53457ab](https://github.com/postgrid/postgrid-python/commit/53457abee1fea7154fd0918aa194f106ff4a9a51))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([899cab3](https://github.com/postgrid/postgrid-python/commit/899cab3df49e481eee336a3e585df7bb58334b0b))
* **readme:** rename PostGrid ([c23572a](https://github.com/postgrid/postgrid-python/commit/c23572aeb87f04560983d0bdc664fecd393bab2a))


### Chores

* **internal:** codegen related update ([3b415ec](https://github.com/postgrid/postgrid-python/commit/3b415ece8193658f82764f82f6e6c55575b3d005))
* **package:** drop Python 3.8 support ([e2e6808](https://github.com/postgrid/postgrid-python/commit/e2e6808b739591baf7258c1ea49fca1d83b09dfc))
* sync repo ([3f005c5](https://github.com/postgrid/postgrid-python/commit/3f005c5c29d1583544b1e55269fe71b07f165d13))
* update SDK settings ([8831e90](https://github.com/postgrid/postgrid-python/commit/8831e903672a9e505744acb42af75da40c816f61))
* update SDK settings ([277f25a](https://github.com/postgrid/postgrid-python/commit/277f25a1fa957073e355fba73bfa783b85adb2ad))
