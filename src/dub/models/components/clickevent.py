"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tagschema import TagSchema, TagSchemaTypedDict
from dub.types import BaseModel, Nullable, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Event(str, Enum):
    CLICK = "click"


class ClickTypedDict(TypedDict):
    id: str
    url: str
    continent: str
    country: str
    city: str
    device: str
    browser: str
    os: str
    referer: str
    referer_url: str
    ip: str
    qr: NotRequired[bool]


class Click(BaseModel):
    id: str

    url: str

    continent: str

    country: str

    city: str

    device: str

    browser: str

    os: str

    referer: str

    referer_url: Annotated[str, pydantic.Field(alias="refererUrl")]

    ip: str

    qr: Optional[bool] = None


class ClickEventGeoTypedDict(TypedDict):
    r"""Geo targeting information for the short link in JSON format `{[COUNTRY]: https://example.com }`. Learn more: https://d.to/geo"""

    af: NotRequired[str]
    al: NotRequired[str]
    dz: NotRequired[str]
    as_: NotRequired[str]
    ad: NotRequired[str]
    ao: NotRequired[str]
    ai: NotRequired[str]
    aq: NotRequired[str]
    ag: NotRequired[str]
    ar: NotRequired[str]
    am: NotRequired[str]
    aw: NotRequired[str]
    au: NotRequired[str]
    at: NotRequired[str]
    az: NotRequired[str]
    bs: NotRequired[str]
    bh: NotRequired[str]
    bd: NotRequired[str]
    bb: NotRequired[str]
    by: NotRequired[str]
    be: NotRequired[str]
    bz: NotRequired[str]
    bj: NotRequired[str]
    bm: NotRequired[str]
    bt: NotRequired[str]
    bo: NotRequired[str]
    ba: NotRequired[str]
    bw: NotRequired[str]
    bv: NotRequired[str]
    br: NotRequired[str]
    io: NotRequired[str]
    bn: NotRequired[str]
    bg: NotRequired[str]
    bf: NotRequired[str]
    bi: NotRequired[str]
    kh: NotRequired[str]
    cm: NotRequired[str]
    ca: NotRequired[str]
    cv: NotRequired[str]
    ky: NotRequired[str]
    cf: NotRequired[str]
    td: NotRequired[str]
    cl: NotRequired[str]
    cn: NotRequired[str]
    cx: NotRequired[str]
    cc: NotRequired[str]
    co: NotRequired[str]
    km: NotRequired[str]
    cg: NotRequired[str]
    cd: NotRequired[str]
    ck: NotRequired[str]
    cr: NotRequired[str]
    ci: NotRequired[str]
    hr: NotRequired[str]
    cu: NotRequired[str]
    cy: NotRequired[str]
    cz: NotRequired[str]
    dk: NotRequired[str]
    dj: NotRequired[str]
    dm: NotRequired[str]
    do: NotRequired[str]
    ec: NotRequired[str]
    eg: NotRequired[str]
    sv: NotRequired[str]
    gq: NotRequired[str]
    er: NotRequired[str]
    ee: NotRequired[str]
    et: NotRequired[str]
    fk: NotRequired[str]
    fo: NotRequired[str]
    fj: NotRequired[str]
    fi: NotRequired[str]
    fr: NotRequired[str]
    gf: NotRequired[str]
    pf: NotRequired[str]
    tf: NotRequired[str]
    ga: NotRequired[str]
    gm: NotRequired[str]
    ge: NotRequired[str]
    de: NotRequired[str]
    gh: NotRequired[str]
    gi: NotRequired[str]
    gr: NotRequired[str]
    gl: NotRequired[str]
    gd: NotRequired[str]
    gp: NotRequired[str]
    gu: NotRequired[str]
    gt: NotRequired[str]
    gn: NotRequired[str]
    gw: NotRequired[str]
    gy: NotRequired[str]
    ht: NotRequired[str]
    hm: NotRequired[str]
    va: NotRequired[str]
    hn: NotRequired[str]
    hk: NotRequired[str]
    hu: NotRequired[str]
    is_: NotRequired[str]
    in_: NotRequired[str]
    id: NotRequired[str]
    ir: NotRequired[str]
    iq: NotRequired[str]
    ie: NotRequired[str]
    il: NotRequired[str]
    it: NotRequired[str]
    jm: NotRequired[str]
    jp: NotRequired[str]
    jo: NotRequired[str]
    kz: NotRequired[str]
    ke: NotRequired[str]
    ki: NotRequired[str]
    kp: NotRequired[str]
    kr: NotRequired[str]
    kw: NotRequired[str]
    kg: NotRequired[str]
    la: NotRequired[str]
    lv: NotRequired[str]
    lb: NotRequired[str]
    ls: NotRequired[str]
    lr: NotRequired[str]
    ly: NotRequired[str]
    li: NotRequired[str]
    lt: NotRequired[str]
    lu: NotRequired[str]
    mo: NotRequired[str]
    mg: NotRequired[str]
    mw: NotRequired[str]
    my: NotRequired[str]
    mv: NotRequired[str]
    ml: NotRequired[str]
    mt: NotRequired[str]
    mh: NotRequired[str]
    mq: NotRequired[str]
    mr: NotRequired[str]
    mu: NotRequired[str]
    yt: NotRequired[str]
    mx: NotRequired[str]
    fm: NotRequired[str]
    md: NotRequired[str]
    mc: NotRequired[str]
    mn: NotRequired[str]
    ms: NotRequired[str]
    ma: NotRequired[str]
    mz: NotRequired[str]
    mm: NotRequired[str]
    na: NotRequired[str]
    nr: NotRequired[str]
    np: NotRequired[str]
    nl: NotRequired[str]
    nc: NotRequired[str]
    nz: NotRequired[str]
    ni: NotRequired[str]
    ne: NotRequired[str]
    ng: NotRequired[str]
    nu: NotRequired[str]
    nf: NotRequired[str]
    mk: NotRequired[str]
    mp: NotRequired[str]
    no: NotRequired[str]
    om: NotRequired[str]
    pk: NotRequired[str]
    pw: NotRequired[str]
    ps: NotRequired[str]
    pa: NotRequired[str]
    pg: NotRequired[str]
    py: NotRequired[str]
    pe: NotRequired[str]
    ph: NotRequired[str]
    pn: NotRequired[str]
    pl: NotRequired[str]
    pt: NotRequired[str]
    pr: NotRequired[str]
    qa: NotRequired[str]
    re: NotRequired[str]
    ro: NotRequired[str]
    ru: NotRequired[str]
    rw: NotRequired[str]
    sh: NotRequired[str]
    kn: NotRequired[str]
    lc: NotRequired[str]
    pm: NotRequired[str]
    vc: NotRequired[str]
    ws: NotRequired[str]
    sm: NotRequired[str]
    st: NotRequired[str]
    sa: NotRequired[str]
    sn: NotRequired[str]
    sc: NotRequired[str]
    sl: NotRequired[str]
    sg: NotRequired[str]
    sk: NotRequired[str]
    si: NotRequired[str]
    sb: NotRequired[str]
    so: NotRequired[str]
    za: NotRequired[str]
    gs: NotRequired[str]
    es: NotRequired[str]
    lk: NotRequired[str]
    sd: NotRequired[str]
    sr: NotRequired[str]
    sj: NotRequired[str]
    sz: NotRequired[str]
    se: NotRequired[str]
    ch: NotRequired[str]
    sy: NotRequired[str]
    tw: NotRequired[str]
    tj: NotRequired[str]
    tz: NotRequired[str]
    th: NotRequired[str]
    tl: NotRequired[str]
    tg: NotRequired[str]
    tk: NotRequired[str]
    to: NotRequired[str]
    tt: NotRequired[str]
    tn: NotRequired[str]
    tr: NotRequired[str]
    tm: NotRequired[str]
    tc: NotRequired[str]
    tv: NotRequired[str]
    ug: NotRequired[str]
    ua: NotRequired[str]
    ae: NotRequired[str]
    gb: NotRequired[str]
    us: NotRequired[str]
    um: NotRequired[str]
    uy: NotRequired[str]
    uz: NotRequired[str]
    vu: NotRequired[str]
    ve: NotRequired[str]
    vn: NotRequired[str]
    vg: NotRequired[str]
    vi: NotRequired[str]
    wf: NotRequired[str]
    eh: NotRequired[str]
    ye: NotRequired[str]
    zm: NotRequired[str]
    zw: NotRequired[str]
    ax: NotRequired[str]
    bq: NotRequired[str]
    cw: NotRequired[str]
    gg: NotRequired[str]
    im: NotRequired[str]
    je: NotRequired[str]
    me: NotRequired[str]
    bl: NotRequired[str]
    mf: NotRequired[str]
    rs: NotRequired[str]
    sx: NotRequired[str]
    ss: NotRequired[str]
    xk: NotRequired[str]


class ClickEventGeo(BaseModel):
    r"""Geo targeting information for the short link in JSON format `{[COUNTRY]: https://example.com }`. Learn more: https://d.to/geo"""

    af: Annotated[Optional[str], pydantic.Field(alias="AF")] = None

    al: Annotated[Optional[str], pydantic.Field(alias="AL")] = None

    dz: Annotated[Optional[str], pydantic.Field(alias="DZ")] = None

    as_: Annotated[Optional[str], pydantic.Field(alias="AS")] = None

    ad: Annotated[Optional[str], pydantic.Field(alias="AD")] = None

    ao: Annotated[Optional[str], pydantic.Field(alias="AO")] = None

    ai: Annotated[Optional[str], pydantic.Field(alias="AI")] = None

    aq: Annotated[Optional[str], pydantic.Field(alias="AQ")] = None

    ag: Annotated[Optional[str], pydantic.Field(alias="AG")] = None

    ar: Annotated[Optional[str], pydantic.Field(alias="AR")] = None

    am: Annotated[Optional[str], pydantic.Field(alias="AM")] = None

    aw: Annotated[Optional[str], pydantic.Field(alias="AW")] = None

    au: Annotated[Optional[str], pydantic.Field(alias="AU")] = None

    at: Annotated[Optional[str], pydantic.Field(alias="AT")] = None

    az: Annotated[Optional[str], pydantic.Field(alias="AZ")] = None

    bs: Annotated[Optional[str], pydantic.Field(alias="BS")] = None

    bh: Annotated[Optional[str], pydantic.Field(alias="BH")] = None

    bd: Annotated[Optional[str], pydantic.Field(alias="BD")] = None

    bb: Annotated[Optional[str], pydantic.Field(alias="BB")] = None

    by: Annotated[Optional[str], pydantic.Field(alias="BY")] = None

    be: Annotated[Optional[str], pydantic.Field(alias="BE")] = None

    bz: Annotated[Optional[str], pydantic.Field(alias="BZ")] = None

    bj: Annotated[Optional[str], pydantic.Field(alias="BJ")] = None

    bm: Annotated[Optional[str], pydantic.Field(alias="BM")] = None

    bt: Annotated[Optional[str], pydantic.Field(alias="BT")] = None

    bo: Annotated[Optional[str], pydantic.Field(alias="BO")] = None

    ba: Annotated[Optional[str], pydantic.Field(alias="BA")] = None

    bw: Annotated[Optional[str], pydantic.Field(alias="BW")] = None

    bv: Annotated[Optional[str], pydantic.Field(alias="BV")] = None

    br: Annotated[Optional[str], pydantic.Field(alias="BR")] = None

    io: Annotated[Optional[str], pydantic.Field(alias="IO")] = None

    bn: Annotated[Optional[str], pydantic.Field(alias="BN")] = None

    bg: Annotated[Optional[str], pydantic.Field(alias="BG")] = None

    bf: Annotated[Optional[str], pydantic.Field(alias="BF")] = None

    bi: Annotated[Optional[str], pydantic.Field(alias="BI")] = None

    kh: Annotated[Optional[str], pydantic.Field(alias="KH")] = None

    cm: Annotated[Optional[str], pydantic.Field(alias="CM")] = None

    ca: Annotated[Optional[str], pydantic.Field(alias="CA")] = None

    cv: Annotated[Optional[str], pydantic.Field(alias="CV")] = None

    ky: Annotated[Optional[str], pydantic.Field(alias="KY")] = None

    cf: Annotated[Optional[str], pydantic.Field(alias="CF")] = None

    td: Annotated[Optional[str], pydantic.Field(alias="TD")] = None

    cl: Annotated[Optional[str], pydantic.Field(alias="CL")] = None

    cn: Annotated[Optional[str], pydantic.Field(alias="CN")] = None

    cx: Annotated[Optional[str], pydantic.Field(alias="CX")] = None

    cc: Annotated[Optional[str], pydantic.Field(alias="CC")] = None

    co: Annotated[Optional[str], pydantic.Field(alias="CO")] = None

    km: Annotated[Optional[str], pydantic.Field(alias="KM")] = None

    cg: Annotated[Optional[str], pydantic.Field(alias="CG")] = None

    cd: Annotated[Optional[str], pydantic.Field(alias="CD")] = None

    ck: Annotated[Optional[str], pydantic.Field(alias="CK")] = None

    cr: Annotated[Optional[str], pydantic.Field(alias="CR")] = None

    ci: Annotated[Optional[str], pydantic.Field(alias="CI")] = None

    hr: Annotated[Optional[str], pydantic.Field(alias="HR")] = None

    cu: Annotated[Optional[str], pydantic.Field(alias="CU")] = None

    cy: Annotated[Optional[str], pydantic.Field(alias="CY")] = None

    cz: Annotated[Optional[str], pydantic.Field(alias="CZ")] = None

    dk: Annotated[Optional[str], pydantic.Field(alias="DK")] = None

    dj: Annotated[Optional[str], pydantic.Field(alias="DJ")] = None

    dm: Annotated[Optional[str], pydantic.Field(alias="DM")] = None

    do: Annotated[Optional[str], pydantic.Field(alias="DO")] = None

    ec: Annotated[Optional[str], pydantic.Field(alias="EC")] = None

    eg: Annotated[Optional[str], pydantic.Field(alias="EG")] = None

    sv: Annotated[Optional[str], pydantic.Field(alias="SV")] = None

    gq: Annotated[Optional[str], pydantic.Field(alias="GQ")] = None

    er: Annotated[Optional[str], pydantic.Field(alias="ER")] = None

    ee: Annotated[Optional[str], pydantic.Field(alias="EE")] = None

    et: Annotated[Optional[str], pydantic.Field(alias="ET")] = None

    fk: Annotated[Optional[str], pydantic.Field(alias="FK")] = None

    fo: Annotated[Optional[str], pydantic.Field(alias="FO")] = None

    fj: Annotated[Optional[str], pydantic.Field(alias="FJ")] = None

    fi: Annotated[Optional[str], pydantic.Field(alias="FI")] = None

    fr: Annotated[Optional[str], pydantic.Field(alias="FR")] = None

    gf: Annotated[Optional[str], pydantic.Field(alias="GF")] = None

    pf: Annotated[Optional[str], pydantic.Field(alias="PF")] = None

    tf: Annotated[Optional[str], pydantic.Field(alias="TF")] = None

    ga: Annotated[Optional[str], pydantic.Field(alias="GA")] = None

    gm: Annotated[Optional[str], pydantic.Field(alias="GM")] = None

    ge: Annotated[Optional[str], pydantic.Field(alias="GE")] = None

    de: Annotated[Optional[str], pydantic.Field(alias="DE")] = None

    gh: Annotated[Optional[str], pydantic.Field(alias="GH")] = None

    gi: Annotated[Optional[str], pydantic.Field(alias="GI")] = None

    gr: Annotated[Optional[str], pydantic.Field(alias="GR")] = None

    gl: Annotated[Optional[str], pydantic.Field(alias="GL")] = None

    gd: Annotated[Optional[str], pydantic.Field(alias="GD")] = None

    gp: Annotated[Optional[str], pydantic.Field(alias="GP")] = None

    gu: Annotated[Optional[str], pydantic.Field(alias="GU")] = None

    gt: Annotated[Optional[str], pydantic.Field(alias="GT")] = None

    gn: Annotated[Optional[str], pydantic.Field(alias="GN")] = None

    gw: Annotated[Optional[str], pydantic.Field(alias="GW")] = None

    gy: Annotated[Optional[str], pydantic.Field(alias="GY")] = None

    ht: Annotated[Optional[str], pydantic.Field(alias="HT")] = None

    hm: Annotated[Optional[str], pydantic.Field(alias="HM")] = None

    va: Annotated[Optional[str], pydantic.Field(alias="VA")] = None

    hn: Annotated[Optional[str], pydantic.Field(alias="HN")] = None

    hk: Annotated[Optional[str], pydantic.Field(alias="HK")] = None

    hu: Annotated[Optional[str], pydantic.Field(alias="HU")] = None

    is_: Annotated[Optional[str], pydantic.Field(alias="IS")] = None

    in_: Annotated[Optional[str], pydantic.Field(alias="IN")] = None

    id: Annotated[Optional[str], pydantic.Field(alias="ID")] = None

    ir: Annotated[Optional[str], pydantic.Field(alias="IR")] = None

    iq: Annotated[Optional[str], pydantic.Field(alias="IQ")] = None

    ie: Annotated[Optional[str], pydantic.Field(alias="IE")] = None

    il: Annotated[Optional[str], pydantic.Field(alias="IL")] = None

    it: Annotated[Optional[str], pydantic.Field(alias="IT")] = None

    jm: Annotated[Optional[str], pydantic.Field(alias="JM")] = None

    jp: Annotated[Optional[str], pydantic.Field(alias="JP")] = None

    jo: Annotated[Optional[str], pydantic.Field(alias="JO")] = None

    kz: Annotated[Optional[str], pydantic.Field(alias="KZ")] = None

    ke: Annotated[Optional[str], pydantic.Field(alias="KE")] = None

    ki: Annotated[Optional[str], pydantic.Field(alias="KI")] = None

    kp: Annotated[Optional[str], pydantic.Field(alias="KP")] = None

    kr: Annotated[Optional[str], pydantic.Field(alias="KR")] = None

    kw: Annotated[Optional[str], pydantic.Field(alias="KW")] = None

    kg: Annotated[Optional[str], pydantic.Field(alias="KG")] = None

    la: Annotated[Optional[str], pydantic.Field(alias="LA")] = None

    lv: Annotated[Optional[str], pydantic.Field(alias="LV")] = None

    lb: Annotated[Optional[str], pydantic.Field(alias="LB")] = None

    ls: Annotated[Optional[str], pydantic.Field(alias="LS")] = None

    lr: Annotated[Optional[str], pydantic.Field(alias="LR")] = None

    ly: Annotated[Optional[str], pydantic.Field(alias="LY")] = None

    li: Annotated[Optional[str], pydantic.Field(alias="LI")] = None

    lt: Annotated[Optional[str], pydantic.Field(alias="LT")] = None

    lu: Annotated[Optional[str], pydantic.Field(alias="LU")] = None

    mo: Annotated[Optional[str], pydantic.Field(alias="MO")] = None

    mg: Annotated[Optional[str], pydantic.Field(alias="MG")] = None

    mw: Annotated[Optional[str], pydantic.Field(alias="MW")] = None

    my: Annotated[Optional[str], pydantic.Field(alias="MY")] = None

    mv: Annotated[Optional[str], pydantic.Field(alias="MV")] = None

    ml: Annotated[Optional[str], pydantic.Field(alias="ML")] = None

    mt: Annotated[Optional[str], pydantic.Field(alias="MT")] = None

    mh: Annotated[Optional[str], pydantic.Field(alias="MH")] = None

    mq: Annotated[Optional[str], pydantic.Field(alias="MQ")] = None

    mr: Annotated[Optional[str], pydantic.Field(alias="MR")] = None

    mu: Annotated[Optional[str], pydantic.Field(alias="MU")] = None

    yt: Annotated[Optional[str], pydantic.Field(alias="YT")] = None

    mx: Annotated[Optional[str], pydantic.Field(alias="MX")] = None

    fm: Annotated[Optional[str], pydantic.Field(alias="FM")] = None

    md: Annotated[Optional[str], pydantic.Field(alias="MD")] = None

    mc: Annotated[Optional[str], pydantic.Field(alias="MC")] = None

    mn: Annotated[Optional[str], pydantic.Field(alias="MN")] = None

    ms: Annotated[Optional[str], pydantic.Field(alias="MS")] = None

    ma: Annotated[Optional[str], pydantic.Field(alias="MA")] = None

    mz: Annotated[Optional[str], pydantic.Field(alias="MZ")] = None

    mm: Annotated[Optional[str], pydantic.Field(alias="MM")] = None

    na: Annotated[Optional[str], pydantic.Field(alias="NA")] = None

    nr: Annotated[Optional[str], pydantic.Field(alias="NR")] = None

    np: Annotated[Optional[str], pydantic.Field(alias="NP")] = None

    nl: Annotated[Optional[str], pydantic.Field(alias="NL")] = None

    nc: Annotated[Optional[str], pydantic.Field(alias="NC")] = None

    nz: Annotated[Optional[str], pydantic.Field(alias="NZ")] = None

    ni: Annotated[Optional[str], pydantic.Field(alias="NI")] = None

    ne: Annotated[Optional[str], pydantic.Field(alias="NE")] = None

    ng: Annotated[Optional[str], pydantic.Field(alias="NG")] = None

    nu: Annotated[Optional[str], pydantic.Field(alias="NU")] = None

    nf: Annotated[Optional[str], pydantic.Field(alias="NF")] = None

    mk: Annotated[Optional[str], pydantic.Field(alias="MK")] = None

    mp: Annotated[Optional[str], pydantic.Field(alias="MP")] = None

    no: Annotated[Optional[str], pydantic.Field(alias="NO")] = None

    om: Annotated[Optional[str], pydantic.Field(alias="OM")] = None

    pk: Annotated[Optional[str], pydantic.Field(alias="PK")] = None

    pw: Annotated[Optional[str], pydantic.Field(alias="PW")] = None

    ps: Annotated[Optional[str], pydantic.Field(alias="PS")] = None

    pa: Annotated[Optional[str], pydantic.Field(alias="PA")] = None

    pg: Annotated[Optional[str], pydantic.Field(alias="PG")] = None

    py: Annotated[Optional[str], pydantic.Field(alias="PY")] = None

    pe: Annotated[Optional[str], pydantic.Field(alias="PE")] = None

    ph: Annotated[Optional[str], pydantic.Field(alias="PH")] = None

    pn: Annotated[Optional[str], pydantic.Field(alias="PN")] = None

    pl: Annotated[Optional[str], pydantic.Field(alias="PL")] = None

    pt: Annotated[Optional[str], pydantic.Field(alias="PT")] = None

    pr: Annotated[Optional[str], pydantic.Field(alias="PR")] = None

    qa: Annotated[Optional[str], pydantic.Field(alias="QA")] = None

    re: Annotated[Optional[str], pydantic.Field(alias="RE")] = None

    ro: Annotated[Optional[str], pydantic.Field(alias="RO")] = None

    ru: Annotated[Optional[str], pydantic.Field(alias="RU")] = None

    rw: Annotated[Optional[str], pydantic.Field(alias="RW")] = None

    sh: Annotated[Optional[str], pydantic.Field(alias="SH")] = None

    kn: Annotated[Optional[str], pydantic.Field(alias="KN")] = None

    lc: Annotated[Optional[str], pydantic.Field(alias="LC")] = None

    pm: Annotated[Optional[str], pydantic.Field(alias="PM")] = None

    vc: Annotated[Optional[str], pydantic.Field(alias="VC")] = None

    ws: Annotated[Optional[str], pydantic.Field(alias="WS")] = None

    sm: Annotated[Optional[str], pydantic.Field(alias="SM")] = None

    st: Annotated[Optional[str], pydantic.Field(alias="ST")] = None

    sa: Annotated[Optional[str], pydantic.Field(alias="SA")] = None

    sn: Annotated[Optional[str], pydantic.Field(alias="SN")] = None

    sc: Annotated[Optional[str], pydantic.Field(alias="SC")] = None

    sl: Annotated[Optional[str], pydantic.Field(alias="SL")] = None

    sg: Annotated[Optional[str], pydantic.Field(alias="SG")] = None

    sk: Annotated[Optional[str], pydantic.Field(alias="SK")] = None

    si: Annotated[Optional[str], pydantic.Field(alias="SI")] = None

    sb: Annotated[Optional[str], pydantic.Field(alias="SB")] = None

    so: Annotated[Optional[str], pydantic.Field(alias="SO")] = None

    za: Annotated[Optional[str], pydantic.Field(alias="ZA")] = None

    gs: Annotated[Optional[str], pydantic.Field(alias="GS")] = None

    es: Annotated[Optional[str], pydantic.Field(alias="ES")] = None

    lk: Annotated[Optional[str], pydantic.Field(alias="LK")] = None

    sd: Annotated[Optional[str], pydantic.Field(alias="SD")] = None

    sr: Annotated[Optional[str], pydantic.Field(alias="SR")] = None

    sj: Annotated[Optional[str], pydantic.Field(alias="SJ")] = None

    sz: Annotated[Optional[str], pydantic.Field(alias="SZ")] = None

    se: Annotated[Optional[str], pydantic.Field(alias="SE")] = None

    ch: Annotated[Optional[str], pydantic.Field(alias="CH")] = None

    sy: Annotated[Optional[str], pydantic.Field(alias="SY")] = None

    tw: Annotated[Optional[str], pydantic.Field(alias="TW")] = None

    tj: Annotated[Optional[str], pydantic.Field(alias="TJ")] = None

    tz: Annotated[Optional[str], pydantic.Field(alias="TZ")] = None

    th: Annotated[Optional[str], pydantic.Field(alias="TH")] = None

    tl: Annotated[Optional[str], pydantic.Field(alias="TL")] = None

    tg: Annotated[Optional[str], pydantic.Field(alias="TG")] = None

    tk: Annotated[Optional[str], pydantic.Field(alias="TK")] = None

    to: Annotated[Optional[str], pydantic.Field(alias="TO")] = None

    tt: Annotated[Optional[str], pydantic.Field(alias="TT")] = None

    tn: Annotated[Optional[str], pydantic.Field(alias="TN")] = None

    tr: Annotated[Optional[str], pydantic.Field(alias="TR")] = None

    tm: Annotated[Optional[str], pydantic.Field(alias="TM")] = None

    tc: Annotated[Optional[str], pydantic.Field(alias="TC")] = None

    tv: Annotated[Optional[str], pydantic.Field(alias="TV")] = None

    ug: Annotated[Optional[str], pydantic.Field(alias="UG")] = None

    ua: Annotated[Optional[str], pydantic.Field(alias="UA")] = None

    ae: Annotated[Optional[str], pydantic.Field(alias="AE")] = None

    gb: Annotated[Optional[str], pydantic.Field(alias="GB")] = None

    us: Annotated[Optional[str], pydantic.Field(alias="US")] = None

    um: Annotated[Optional[str], pydantic.Field(alias="UM")] = None

    uy: Annotated[Optional[str], pydantic.Field(alias="UY")] = None

    uz: Annotated[Optional[str], pydantic.Field(alias="UZ")] = None

    vu: Annotated[Optional[str], pydantic.Field(alias="VU")] = None

    ve: Annotated[Optional[str], pydantic.Field(alias="VE")] = None

    vn: Annotated[Optional[str], pydantic.Field(alias="VN")] = None

    vg: Annotated[Optional[str], pydantic.Field(alias="VG")] = None

    vi: Annotated[Optional[str], pydantic.Field(alias="VI")] = None

    wf: Annotated[Optional[str], pydantic.Field(alias="WF")] = None

    eh: Annotated[Optional[str], pydantic.Field(alias="EH")] = None

    ye: Annotated[Optional[str], pydantic.Field(alias="YE")] = None

    zm: Annotated[Optional[str], pydantic.Field(alias="ZM")] = None

    zw: Annotated[Optional[str], pydantic.Field(alias="ZW")] = None

    ax: Annotated[Optional[str], pydantic.Field(alias="AX")] = None

    bq: Annotated[Optional[str], pydantic.Field(alias="BQ")] = None

    cw: Annotated[Optional[str], pydantic.Field(alias="CW")] = None

    gg: Annotated[Optional[str], pydantic.Field(alias="GG")] = None

    im: Annotated[Optional[str], pydantic.Field(alias="IM")] = None

    je: Annotated[Optional[str], pydantic.Field(alias="JE")] = None

    me: Annotated[Optional[str], pydantic.Field(alias="ME")] = None

    bl: Annotated[Optional[str], pydantic.Field(alias="BL")] = None

    mf: Annotated[Optional[str], pydantic.Field(alias="MF")] = None

    rs: Annotated[Optional[str], pydantic.Field(alias="RS")] = None

    sx: Annotated[Optional[str], pydantic.Field(alias="SX")] = None

    ss: Annotated[Optional[str], pydantic.Field(alias="SS")] = None

    xk: Annotated[Optional[str], pydantic.Field(alias="XK")] = None


class LinkTypedDict(TypedDict):
    id: str
    r"""The unique ID of the short link."""
    domain: str
    r"""The domain of the short link. If not provided, the primary domain for the workspace will be used (or `dub.sh` if the workspace has no domains)."""
    key: str
    r"""The short link slug. If not provided, a random 7-character slug will be generated."""
    external_id: Nullable[str]
    r"""This is the ID of the link in your database. If set, it can be used to identify the link in the future. Must be prefixed with 'ext_' when passed as a query parameter."""
    url: str
    expires_at: str
    expired_url: Nullable[str]
    r"""The URL to redirect to when the short link has expired."""
    password: Nullable[str]
    r"""The password required to access the destination URL of the short link."""
    title: Nullable[str]
    r"""The title of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    description: Nullable[str]
    r"""The description of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    image: Nullable[str]
    r"""The image of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""
    video: Nullable[str]
    r"""The custom link preview video (og:video). Will be used for Custom Social Media Cards if `proxy` is true. Learn more: https://d.to/og"""
    ios: Nullable[str]
    r"""The iOS destination URL for the short link for iOS device targeting."""
    android: Nullable[str]
    r"""The Android destination URL for the short link for Android device targeting."""
    geo: Nullable[ClickEventGeoTypedDict]
    r"""Geo targeting information for the short link in JSON format `{[COUNTRY]: https://example.com }`. Learn more: https://d.to/geo"""
    tag_id: Nullable[str]
    r"""The unique ID of the tag assigned to the short link. This field is deprecated – use `tags` instead."""
    tags: Nullable[List[TagSchemaTypedDict]]
    r"""The tags assigned to the short link."""
    comments: Nullable[str]
    r"""The comments for the short link."""
    short_link: str
    r"""The full URL of the short link, including the https protocol (e.g. `https://dub.sh/try`)."""
    qr_code: str
    r"""The full URL of the QR code for the short link (e.g. `https://api.dub.co/qr?url=https://dub.sh/try`)."""
    utm_source: Nullable[str]
    r"""The UTM source of the short link."""
    utm_medium: Nullable[str]
    r"""The UTM medium of the short link."""
    utm_campaign: Nullable[str]
    r"""The UTM campaign of the short link."""
    utm_term: Nullable[str]
    r"""The UTM term of the short link."""
    utm_content: Nullable[str]
    r"""The UTM content of the short link."""
    user_id: Nullable[str]
    workspace_id: str
    r"""The workspace ID of the short link."""
    last_clicked: str
    created_at: str
    updated_at: str
    project_id: str
    r"""The project ID of the short link. This field is deprecated – use `workspaceId` instead."""
    track_conversion: NotRequired[bool]
    archived: NotRequired[bool]
    proxy: NotRequired[bool]
    rewrite: NotRequired[bool]
    do_index: NotRequired[bool]
    public_stats: NotRequired[bool]
    clicks: NotRequired[float]
    r"""The number of clicks on the short link."""
    leads: NotRequired[float]
    r"""[BETA]: The number of leads the short links has generated."""
    sales: NotRequired[float]
    r"""[BETA]: The number of sales the short links has generated."""
    sale_amount: NotRequired[float]
    r"""[BETA]: The total dollar amount of sales the short links has generated (in cents)."""


class Link(BaseModel):
    id: str
    r"""The unique ID of the short link."""

    domain: str
    r"""The domain of the short link. If not provided, the primary domain for the workspace will be used (or `dub.sh` if the workspace has no domains)."""

    key: str
    r"""The short link slug. If not provided, a random 7-character slug will be generated."""

    external_id: Annotated[Nullable[str], pydantic.Field(alias="externalId")]
    r"""This is the ID of the link in your database. If set, it can be used to identify the link in the future. Must be prefixed with 'ext_' when passed as a query parameter."""

    url: str

    expires_at: Annotated[str, pydantic.Field(alias="expiresAt")]

    expired_url: Annotated[Nullable[str], pydantic.Field(alias="expiredUrl")]
    r"""The URL to redirect to when the short link has expired."""

    password: Nullable[str]
    r"""The password required to access the destination URL of the short link."""

    title: Nullable[str]
    r"""The title of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""

    description: Nullable[str]
    r"""The description of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""

    image: Nullable[str]
    r"""The image of the short link generated via `api.dub.co/metatags`. Will be used for Custom Social Media Cards if `proxy` is true."""

    video: Nullable[str]
    r"""The custom link preview video (og:video). Will be used for Custom Social Media Cards if `proxy` is true. Learn more: https://d.to/og"""

    ios: Nullable[str]
    r"""The iOS destination URL for the short link for iOS device targeting."""

    android: Nullable[str]
    r"""The Android destination URL for the short link for Android device targeting."""

    geo: Nullable[ClickEventGeo]
    r"""Geo targeting information for the short link in JSON format `{[COUNTRY]: https://example.com }`. Learn more: https://d.to/geo"""

    tag_id: Annotated[
        Nullable[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="tagId",
        ),
    ]
    r"""The unique ID of the tag assigned to the short link. This field is deprecated – use `tags` instead."""

    tags: Nullable[List[TagSchema]]
    r"""The tags assigned to the short link."""

    comments: Nullable[str]
    r"""The comments for the short link."""

    short_link: Annotated[str, pydantic.Field(alias="shortLink")]
    r"""The full URL of the short link, including the https protocol (e.g. `https://dub.sh/try`)."""

    qr_code: Annotated[str, pydantic.Field(alias="qrCode")]
    r"""The full URL of the QR code for the short link (e.g. `https://api.dub.co/qr?url=https://dub.sh/try`)."""

    utm_source: Nullable[str]
    r"""The UTM source of the short link."""

    utm_medium: Nullable[str]
    r"""The UTM medium of the short link."""

    utm_campaign: Nullable[str]
    r"""The UTM campaign of the short link."""

    utm_term: Nullable[str]
    r"""The UTM term of the short link."""

    utm_content: Nullable[str]
    r"""The UTM content of the short link."""

    user_id: Annotated[Nullable[str], pydantic.Field(alias="userId")]

    workspace_id: Annotated[str, pydantic.Field(alias="workspaceId")]
    r"""The workspace ID of the short link."""

    last_clicked: Annotated[str, pydantic.Field(alias="lastClicked")]

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]

    updated_at: Annotated[str, pydantic.Field(alias="updatedAt")]

    project_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="projectId",
        ),
    ]
    r"""The project ID of the short link. This field is deprecated – use `workspaceId` instead."""

    track_conversion: Annotated[
        Optional[bool], pydantic.Field(alias="trackConversion")
    ] = None

    archived: Optional[bool] = None

    proxy: Optional[bool] = None

    rewrite: Optional[bool] = None

    do_index: Annotated[Optional[bool], pydantic.Field(alias="doIndex")] = None

    public_stats: Annotated[Optional[bool], pydantic.Field(alias="publicStats")] = None

    clicks: Optional[float] = 0
    r"""The number of clicks on the short link."""

    leads: Optional[float] = 0
    r"""[BETA]: The number of leads the short links has generated."""

    sales: Optional[float] = 0
    r"""[BETA]: The number of sales the short links has generated."""

    sale_amount: Annotated[Optional[float], pydantic.Field(alias="saleAmount")] = 0
    r"""[BETA]: The total dollar amount of sales the short links has generated (in cents)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "trackConversion",
            "archived",
            "proxy",
            "rewrite",
            "doIndex",
            "publicStats",
            "clicks",
            "leads",
            "sales",
            "saleAmount",
        ]
        nullable_fields = [
            "externalId",
            "expiredUrl",
            "password",
            "title",
            "description",
            "image",
            "video",
            "ios",
            "android",
            "geo",
            "tagId",
            "tags",
            "comments",
            "utm_source",
            "utm_medium",
            "utm_campaign",
            "utm_term",
            "utm_content",
            "userId",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class ClickEventTypedDict(TypedDict):
    event: Event
    click: ClickTypedDict
    link: LinkTypedDict
    click_id: str
    r"""Deprecated. Use `click.id` instead."""
    link_id: str
    r"""Deprecated. Use `link.id` instead."""
    domain: str
    r"""Deprecated. Use `link.domain` instead."""
    key: str
    r"""Deprecated. Use `link.key` instead."""
    url: str
    r"""Deprecated. Use `click.url` instead."""
    continent: str
    r"""Deprecated. Use `click.continent` instead."""
    country: str
    r"""Deprecated. Use `click.country` instead."""
    city: str
    r"""Deprecated. Use `click.city` instead."""
    device: str
    r"""Deprecated. Use `click.device` instead."""
    browser: str
    r"""Deprecated. Use `click.browser` instead."""
    os: str
    r"""Deprecated. Use `click.os` instead."""
    qr: float
    r"""Deprecated. Use `click.qr` instead."""
    ip: str
    r"""Deprecated. Use `click.ip` instead."""
    timestamp: NotRequired[str]


class ClickEvent(BaseModel):
    event: Event

    click: Click

    link: Link

    click_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.id` instead."""

    link_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `link.id` instead."""

    domain: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `link.domain` instead."""

    key: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `link.key` instead."""

    url: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.url` instead."""

    continent: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.continent` instead."""

    country: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.country` instead."""

    city: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.city` instead."""

    device: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.device` instead."""

    browser: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.browser` instead."""

    os: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.os` instead."""

    qr: Annotated[
        float,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.qr` instead."""

    ip: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated. Use `click.ip` instead."""

    timestamp: Optional[str] = None
