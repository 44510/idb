#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from argparse import Namespace

from idb.cli import ClientCommand
from idb.common.types import Client


class FocusCommand(ClientCommand):
    @property
    def description(self) -> str:
        return "Brings the simulator window to front"

    @property
    def name(self) -> str:
        return "focus"

    async def run_with_client(self, args: Namespace, client: Client) -> None:
        await client.focus()
